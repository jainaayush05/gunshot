from reports.models import GsFunnelDataMonthly,GsFunnelLabel,Report,VtigerGroups,GsReportFunnelMultiple,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf,GsReportFunnel
from reports.serializers import GsFunnelDataMonthlySerializer ,GsFunnelLabelSerializer,GsReportFunnelMultipleSerializer,ReportSerializer, VtigerLeadaddressSerializer, VtigerLeaddetailsSerializer, VtigerCrmentitySerializer,GsReportFunnelSerializer
from django.db.models import Q
from django.utils import timezone
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, pdfkit
from django.shortcuts import render,redirect
import datetime
from django.core.mail import EmailMessage
from django.db.models import Sum,Count
from django.db import connection
import crypt
import urllib2
import gunshot.settings as settings
def encryptPassword(nameStr, passStr):
        salt = nameStr[0:2]
        salt = '$1$' + salt.ljust(9,'0')
        return crypt.crypt(passStr, salt)


class CreateLead(APIView):
    """
    Create a lead in VTigerCRM
    """

    def post(self, request, format=None):
        ##Push Lead
        data =request.POST.get('lead_data', False)
        email =request.POST.get('email', False)
        url =settings.CRM_URL+'modules/Webforms/post.php/'
        http_headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}
        req = urllib2.Request(url, data, http_headers)
        #import ipdb;ipdb.set_trace();
        response = urllib2.urlopen(req)

        ##Get Lead Number
        url =settings.CRM_URL+'modules/harry/post.php/'
        data = "getlead=1&email="+email
        req = urllib2.Request(url, data, http_headers)
        lead_no = urllib2.urlopen(req).read()

        ##Create Account
        data =request.POST.get('account_data', False)
        data=data+lead_no
        url =settings.CRM_URL+'modules/Webforms/post.php/'
        req = urllib2.Request(url, data, http_headers)
        response1 = urllib2.urlopen(req).read()

        #update lead with lead number and region
        gs_id =request.POST.get('gs_id', False)
        region =request.POST.get('region', False)
        gs= GsReportFunnel.objects.get(id= gs_id)
        gs.lead_no= lead_no
        gs.region = region
        gs.save()

        ## Assign Lead
        user_id =request.POST.get('assigned_name', False)
        if user_id:
            user = VtigerUsers.objects.get(id = user_id)
            url =settings.CRM_URL+'vtigercrm/modules/harry/post.php/'
            data = "lead_no="+lead_no+"&assign="+user.user_name
            req = urllib2.Request(url, data, http_headers)
            response = urllib2.urlopen(req).read()
            gs= GsReportFunnel.objects.get(id= gs_id)
            gs.assgn_first_name= user.first_name
            gs.save()
        
        return Response(response)

class Authentication(APIView):
    """
    Authentication

    """
    def get(self, request, format=None):
        uname = request.GET.get('uname', False)
        password= request.GET.get('pass', False)
        enc_pass = encryptPassword(uname, password)
        user = VtigerUsers.objects.filter(user_name= uname, user_password= enc_pass)
        if len(user) >0:
            request.session['user_id'] = user[0].id
            request.session['user_name'] = user[0].user_name
            request.session['first_name'] = user[0].first_name
            request.session['last_name'] = user[0].last_name
            return Response(True)
        else:
            return Response(False)

class Login(APIView):
    """
    login

    """
    def get(self, request, format=None):
        if request.session.get('user_id', False):
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {})

class Logout(APIView):
    """
    logout

    """
    def get(self, request, format=None):
        try:
            del request.session['user_id']
            del request.session['user_name']
            del request.session['first_name']
            del request.session['last_name']
        except KeyError:
            pass
        return redirect('/login')

class Dashboard(APIView):
    """
    Dashboard

    """
    def get(self, request, format=None):
       if request.session.get('user_id', False):
            name = request.session.get('first_name', False)
            return render(request, 'dashboard.html', {"name":name})
       else:
            return redirect('/login')

class Transactions(APIView):
    """
    List of transaction

    """
    def get(self, request, format=None):
       if request.session.get('user_id', False):
            name = request.session.get('first_name', False)
            type = request.GET.get('type', False)
            date = request.GET.get('date', False)
            if type:
                if date:
                    gs = GsReportFunnel.objects.filter(result=type, created__gte = date)
                else:
                    gs = GsReportFunnel.objects.filter(result=type)
                return render(request, 'transactions.html', {'root_url':settings.ROOT_URL,"gs":gs,"name":name})
            else:
                gs = GsReportFunnel.objects.all()
                return render(request, 'transactions.html', {'root_url':settings.ROOT_URL,"gs":gs,"name":name})
       else:
            return redirect('/login')

class ReportList(APIView):
    """
    List all reports, or create a new report.
    """
    def get(self, request, format=None):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportDetail(APIView):
    """
    Retrieve, update or delete a report instance.
    """
    def get_object(self, pk):
        try:
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = ReportSerializer(report, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CrmData(APIView):
   
    def get(self, request,format=None):
        email = request.GET.get('email', False)
        payments_hdfc_id= request.GET.get('id', False)
        currency=request.GET.get('currency', False)
        amount=request.GET.get('amount', False)
        payment_id=request.GET.get('payment_id', False)
        result=request.GET.get('result', False)
        tran_id=request.GET.get('tran_id', False)
        details=postdate=request.GET.get('details', False)
        auth=request.GET.get('auth', False)
        error=request.GET.get('error', False)
        error_msg=request.GET.get('error_msg', False)
        phone = request.GET.get('phone', False)
        udf1=request.GET.get('udf1', False)
        udf2=request.GET.get('udf2', False)
        udf3=request.GET.get('udf3', False)
        udf4=request.GET.get('udf4', False)
        udf5=request.GET.get('udf5', False)
        product_id=request.GET.get('product_id', False)
        created= request.GET.get('created', False)
        source=request.GET.get('source', False)
        converted_amount=request.GET.get('converted_amount', False)
        region=request.GET.get('region', False)
        flag = False
        if result:
            if result.lower() =="captured":
                flag= True


        if flag:
            if(phone and email):
                det_list= VtigerLeaddetails.objects.filter(email=email)
                add_list= VtigerLeadaddress.objects.filter(Q(mobile=phone)|Q(phone=phone))
                det_list_ids= []
                add_list_ids= []
                final_det_arr= []
                final_add_arr= []
                final_crm_entity_arr=[]
                final_user_arr=[]
                final_group_arr=[]
                final_cf_arr=[]
                for det in det_list:
                    det_list_ids.append(det.leadid)
                for add in add_list:
                    add_list_ids.append(add.leadaddressid)
                list_ids = set(det_list_ids) & set(add_list_ids)
                users_index=[]
                groups_index=[]
                i=0
                for ids in list_ids:
                    det = VtigerLeaddetails.objects.get(leadid =ids)
                    add = VtigerLeadaddress.objects.get(leadaddressid =ids)
                    crm_entity = VtigerCrmentity.objects.get(crmid= ids)
                    cf = VtigerLeadscf.objects.get(leadid= ids)
                    try:
                        user= VtigerUsers.objects.get(id = crm_entity.smownerid)
                        final_user_arr.append(user)
                        users_index.append(i)
                    except:
                        group = VtigerGroups.objects.get(groupid = crm_entity.smownerid)
                        final_group_arr.append(group)
                        groups_index.append(i)

                    final_det_arr.append(det)
                    final_add_arr.append(add)
                    final_crm_entity_arr.append(crm_entity)
                    final_cf_arr.append(cf)
                    i=i+1

                if len(list_ids) == 1:
                    if len(final_user_arr) ==1:
                        gs= GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_user_arr[0].first_name if final_user_arr[0].first_name else '-'),assgn_last_name=(final_user_arr[0].last_name if final_user_arr[0].last_name else '-'),smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="no",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                        gs.save()
                        return Response(GsReportFunnelSerializer(gs).data)
                    else:
                        gs= GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_group_arr[0].groupname if final_group_arr[0].groupname else '-'),assgn_last_name="group",smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="no",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                        gs.save()
                        return Response(GsReportFunnelSerializer(gs).data)
                elif len(list_ids) == 0:
                    gs= GsReportFunnel(leadid='0', city='-', state='-', pobox='-', country='-',phone='-',mobile='-',assgn_first_name='-',assgn_last_name='-',smownerid='0',description='-',createdtime='1992-01-01T12:00:00',modifiedtime='1992-01-01T12:00:00',lead_no='-',email='-',firstname='-',lastname='-',company='-',leadstatus='-',leadsource='-',course='-',campaign_id='-',google_keyword='-',ref_domain='-',traffic_src='-',google_cookie='-',verified="no",has_multiple_leads="no",payments_hdfc_id=(payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                    gs.save()
                    return Response(GsReportFunnelSerializer(gs).data)
                else:
                    if len(users_index)>0:
                        if 0 in users_index:
                            gs=GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_user_arr[0].first_name if final_user_arr[0].first_name else '-'),assgn_last_name=(final_user_arr[0].last_name if final_user_arr[0].last_name else '-'),smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                            gs.save()
                    if len(groups_index)>0:
                        if 0 in groups_index:
                            gs=GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_group_arr[0].groupname if final_group_arr[0].groupname else '-'),assgn_last_name="Group",smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                            gs.save()
                    for i in range(0, len(list_ids)):
                        if i in users_index:
                            GsReportFunnelMultiple(leadid=(final_det_arr[i].leadid if final_det_arr[i].leadid else '-'),gs_id= gs.id, city=(final_add_arr[i].city if final_add_arr[i].city else '-'), state=(final_add_arr[i].state if final_add_arr[i].state else '-'), pobox=(final_add_arr[i].pobox if final_add_arr[i].pobox else '-'), country=(final_add_arr[i].country if final_add_arr[i].country else '-'),phone=(final_add_arr[i].phone if final_add_arr[i].phone else '-'),mobile=(final_add_arr[i].mobile if final_add_arr[i].mobile else '-'),assgn_first_name=(final_user_arr[users_index.index(i)].first_name if final_user_arr[users_index.index(i)].first_name else '-'),assgn_last_name=(final_user_arr[users_index.index(i)].last_name if final_user_arr[users_index.index(i)].last_name else '-'),smownerid=( final_crm_entity_arr[i].smownerid if final_crm_entity_arr[i].smownerid else '-'),description=(final_crm_entity_arr[i].description if final_crm_entity_arr[i].description else '-'),createdtime=(final_crm_entity_arr[i].createdtime if final_crm_entity_arr[i].createdtime else '-'),modifiedtime=(final_crm_entity_arr[i].modifiedtime if final_crm_entity_arr[i].modifiedtime else '-'),lead_no=(final_det_arr[i].lead_no if final_det_arr[i].lead_no else '-'),email=(final_det_arr[i].email if final_det_arr[i].email else '-'),firstname=(final_det_arr[i].firstname if final_det_arr[i].firstname else '-'),lastname=(final_det_arr[i].lastname if final_det_arr[i].lastname else '-'),company=(final_det_arr[i].company if final_det_arr[i].company else '-'),leadstatus=(final_det_arr[i].leadstatus if final_det_arr[i].leadstatus else '-'),leadsource=(final_det_arr[i].leadsource if final_det_arr[i].leadsource else '-'),course=( final_cf_arr[i].cf_607 if final_cf_arr[i].cf_607 else '-'),campaign_id=(final_cf_arr[i].cf_609 if final_cf_arr[i].cf_609 else '-'),google_keyword=(final_cf_arr[i].cf_632 if final_cf_arr[i].cf_632 else '-'),ref_domain=(final_cf_arr[i].cf_633 if final_cf_arr[i].cf_633 else '-'),traffic_src=( final_cf_arr[i].cf_679 if final_cf_arr[i].cf_679 else '-'),google_cookie=(final_cf_arr[i].cf_689 if final_cf_arr[i].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-')).save()
                        else:
                            GsReportFunnelMultiple(leadid=(final_det_arr[i].leadid if final_det_arr[i].leadid else '-'),gs_id= gs.id, city=(final_add_arr[i].city if final_add_arr[i].city else '-'), state=(final_add_arr[i].state if final_add_arr[i].state else '-'), pobox=(final_add_arr[i].pobox if final_add_arr[i].pobox else '-'), country=(final_add_arr[i].country if final_add_arr[i].country else '-'),phone=(final_add_arr[i].phone if final_add_arr[i].phone else '-'),mobile=(final_add_arr[i].mobile if final_add_arr[i].mobile else '-'),assgn_first_name=(final_group_arr[groups_index.index(i)].groupname if final_group_arr[groups_index.index(i)].groupname else '-'),assgn_last_name="Group",smownerid=( final_crm_entity_arr[i].smownerid if final_crm_entity_arr[i].smownerid else '-'),description=(final_crm_entity_arr[i].description if final_crm_entity_arr[i].description else '-'),createdtime=(final_crm_entity_arr[i].createdtime if final_crm_entity_arr[i].createdtime else '-'),modifiedtime=(final_crm_entity_arr[i].modifiedtime if final_crm_entity_arr[i].modifiedtime else '-'),lead_no=(final_det_arr[i].lead_no if final_det_arr[i].lead_no else '-'),email=(final_det_arr[i].email if final_det_arr[i].email else '-'),firstname=(final_det_arr[i].firstname if final_det_arr[i].firstname else '-'),lastname=(final_det_arr[i].lastname if final_det_arr[i].lastname else '-'),company=(final_det_arr[i].company if final_det_arr[i].company else '-'),leadstatus=(final_det_arr[i].leadstatus if final_det_arr[i].leadstatus else '-'),leadsource=(final_det_arr[i].leadsource if final_det_arr[i].leadsource else '-'),course=( final_cf_arr[i].cf_607 if final_cf_arr[i].cf_607 else '-'),campaign_id=(final_cf_arr[i].cf_609 if final_cf_arr[i].cf_609 else '-'),google_keyword=(final_cf_arr[i].cf_632 if final_cf_arr[i].cf_632 else '-'),ref_domain=(final_cf_arr[i].cf_633 if final_cf_arr[i].cf_633 else '-'),traffic_src=( final_cf_arr[i].cf_679 if final_cf_arr[i].cf_679 else '-'),google_cookie=(final_cf_arr[i].cf_689 if final_cf_arr[i].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-')).save()
                    return Response(GsReportFunnelSerializer(gs).data)
            elif(email):
                det_list= VtigerLeaddetails.objects.filter(email=email)
                det_list_ids= []
                final_det_arr= []
                final_add_arr= []
                final_crm_entity_arr=[]
                final_user_arr=[]
                final_group_arr=[]
                final_cf_arr=[]
                users_index=[]
                groups_index=[]
                i=0
                for det in det_list:
                    det_list_ids.append(det.leadid)
                
                for ids in det_list_ids:
                    det = VtigerLeaddetails.objects.get(leadid =ids)
                    add = VtigerLeadaddress.objects.get(leadaddressid =ids)
                    crm_entity = VtigerCrmentity.objects.get(crmid= ids)
                    cf = VtigerLeadscf.objects.get(leadid= ids)
                    try:
                        user= VtigerUsers.objects.get(id = crm_entity.smownerid)
                        final_user_arr.append(user)
                    except:
                        group = VtigerGroups.objects.get(groupid = crm_entity.smownerid)
                        final_group_arr.append(group)
                        
                    final_det_arr.append(det)
                    final_add_arr.append(add)
                    final_crm_entity_arr.append(crm_entity)
                    final_cf_arr.append(cf)
                    i=i+1
                
                if len(det_list_ids) == 1:
                    if len(final_user_arr) ==1:
                        gs= GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_user_arr[0].first_name if final_user_arr[0].first_name else '-'),assgn_last_name=(final_user_arr[0].last_name if final_user_arr[0].last_name else '-'),smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="no",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                        gs.save()
                        return Response(GsReportFunnelSerializer(gs).data)
                    else:
                        gs= GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_group_arr[0].groupname if final_group_arr[0].groupname else '-'),assgn_last_name="group",smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="no",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                        gs.save()
                        return Response(GsReportFunnelSerializer(gs).data)
                elif len(det_list_ids) == 0:
                    gs= GsReportFunnel(leadid='0', city='-', state='-', pobox='-', country='-',phone='-',mobile='-',assgn_first_name='-',assgn_last_name='-',smownerid='0',description='-',createdtime='1992-01-01T12:00:00',modifiedtime='1992-01-01T12:00:00',lead_no='-',email='-',firstname='-',lastname='-',company='-',leadstatus='-',leadsource='-',course='-',campaign_id='-',google_keyword='-',ref_domain='-',traffic_src='-',google_cookie='-',verified="no",has_multiple_leads="no",payments_hdfc_id=(payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                    gs.save()
                    return Response(GsReportFunnelSerializer(gs).data)
                else:
                    if len(users_index)>0:
                        if 0 in users_index:
                            gs=GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_user_arr[0].first_name if final_user_arr[0].first_name else '-'),assgn_last_name=(final_user_arr[0].last_name if final_user_arr[0].last_name else '-'),smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                            gs.save()
                    if len(groups_index)>0:
                        if 0 in groups_index:
                            gs=GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_group_arr[0].groupname if final_group_arr[0].groupname else '-'),assgn_last_name="Group",smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                            gs.save()
                    for i in range(0, len(det_list_ids)):
                        if i in users_index:
                            GsReportFunnelMultiple(leadid=(final_det_arr[i].leadid if final_det_arr[i].leadid else '-'),gs_id= gs.id, city=(final_add_arr[i].city if final_add_arr[i].city else '-'), state=(final_add_arr[i].state if final_add_arr[i].state else '-'), pobox=(final_add_arr[i].pobox if final_add_arr[i].pobox else '-'), country=(final_add_arr[i].country if final_add_arr[i].country else '-'),phone=(final_add_arr[i].phone if final_add_arr[i].phone else '-'),mobile=(final_add_arr[i].mobile if final_add_arr[i].mobile else '-'),assgn_first_name=(final_user_arr[users_index.index(i)].first_name if final_user_arr[users_index.index(i)].first_name else '-'),assgn_last_name=(final_user_arr[users_index.index(i)].last_name if final_user_arr[users_index.index(i)].last_name else '-'),smownerid=( final_crm_entity_arr[i].smownerid if final_crm_entity_arr[i].smownerid else '-'),description=(final_crm_entity_arr[i].description if final_crm_entity_arr[i].description else '-'),createdtime=(final_crm_entity_arr[i].createdtime if final_crm_entity_arr[i].createdtime else '-'),modifiedtime=(final_crm_entity_arr[i].modifiedtime if final_crm_entity_arr[i].modifiedtime else '-'),lead_no=(final_det_arr[i].lead_no if final_det_arr[i].lead_no else '-'),email=(final_det_arr[i].email if final_det_arr[i].email else '-'),firstname=(final_det_arr[i].firstname if final_det_arr[i].firstname else '-'),lastname=(final_det_arr[i].lastname if final_det_arr[i].lastname else '-'),company=(final_det_arr[i].company if final_det_arr[i].company else '-'),leadstatus=(final_det_arr[i].leadstatus if final_det_arr[i].leadstatus else '-'),leadsource=(final_det_arr[i].leadsource if final_det_arr[i].leadsource else '-'),course=( final_cf_arr[i].cf_607 if final_cf_arr[i].cf_607 else '-'),campaign_id=(final_cf_arr[i].cf_609 if final_cf_arr[i].cf_609 else '-'),google_keyword=(final_cf_arr[i].cf_632 if final_cf_arr[i].cf_632 else '-'),ref_domain=(final_cf_arr[i].cf_633 if final_cf_arr[i].cf_633 else '-'),traffic_src=( final_cf_arr[i].cf_679 if final_cf_arr[i].cf_679 else '-'),google_cookie=(final_cf_arr[i].cf_689 if final_cf_arr[i].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-')).save()
                        else:
                            GsReportFunnelMultiple(leadid=(final_det_arr[i].leadid if final_det_arr[i].leadid else '-'),gs_id= gs.id, city=(final_add_arr[i].city if final_add_arr[i].city else '-'), state=(final_add_arr[i].state if final_add_arr[i].state else '-'), pobox=(final_add_arr[i].pobox if final_add_arr[i].pobox else '-'), country=(final_add_arr[i].country if final_add_arr[i].country else '-'),phone=(final_add_arr[i].phone if final_add_arr[i].phone else '-'),mobile=(final_add_arr[i].mobile if final_add_arr[i].mobile else '-'),assgn_first_name=(final_group_arr[groups_index.index(i)].groupname if final_group_arr[groups_index.index(i)].groupname else '-'),assgn_last_name="Group",smownerid=( final_crm_entity_arr[i].smownerid if final_crm_entity_arr[i].smownerid else '-'),description=(final_crm_entity_arr[i].description if final_crm_entity_arr[i].description else '-'),createdtime=(final_crm_entity_arr[i].createdtime if final_crm_entity_arr[i].createdtime else '-'),modifiedtime=(final_crm_entity_arr[i].modifiedtime if final_crm_entity_arr[i].modifiedtime else '-'),lead_no=(final_det_arr[i].lead_no if final_det_arr[i].lead_no else '-'),email=(final_det_arr[i].email if final_det_arr[i].email else '-'),firstname=(final_det_arr[i].firstname if final_det_arr[i].firstname else '-'),lastname=(final_det_arr[i].lastname if final_det_arr[i].lastname else '-'),company=(final_det_arr[i].company if final_det_arr[i].company else '-'),leadstatus=(final_det_arr[i].leadstatus if final_det_arr[i].leadstatus else '-'),leadsource=(final_det_arr[i].leadsource if final_det_arr[i].leadsource else '-'),course=( final_cf_arr[i].cf_607 if final_cf_arr[i].cf_607 else '-'),campaign_id=(final_cf_arr[i].cf_609 if final_cf_arr[i].cf_609 else '-'),google_keyword=(final_cf_arr[i].cf_632 if final_cf_arr[i].cf_632 else '-'),ref_domain=(final_cf_arr[i].cf_633 if final_cf_arr[i].cf_633 else '-'),traffic_src=( final_cf_arr[i].cf_679 if final_cf_arr[i].cf_679 else '-'),google_cookie=(final_cf_arr[i].cf_689 if final_cf_arr[i].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-')).save()
                    return Response(GsReportFunnelSerializer(gs).data)

            else:
                add_list= VtigerLeadaddress.objects.filter(Q(mobile=phone)|Q(phone=phone))
                add_list_ids= []
                final_det_arr= []
                final_add_arr= []
                final_crm_entity_arr=[]
                final_user_arr=[]
                final_group_arr=[]
                final_cf_arr=[]
                users_index=[]
                groups_index=[]
                i=0
                for add in add_list:
                    add_list_ids.append(add.leadaddressid)
                
                for ids in add_list_ids:
                    det = VtigerLeaddetails.objects.get(leadid =ids)
                    add = VtigerLeadaddress.objects.get(leadaddressid =ids)
                    crm_entity = VtigerCrmentity.objects.get(crmid= ids)
                    cf = VtigerLeadscf.objects.get(leadid= ids)
                    try:
                        user= VtigerUsers.objects.get(id = crm_entity.smownerid)
                        final_user_arr.append(user)
                        users_index.append(i)
                    except:
                        group = VtigerGroups.objects.get(groupid = crm_entity.smownerid)
                        final_group_arr.append(group)
                        groups_index.append(i)

                    final_det_arr.append(det)
                    final_add_arr.append(add)
                    final_crm_entity_arr.append(crm_entity)
                    final_cf_arr.append(cf)
                    i=i+1
                if len(add_list_ids) == 1:
                    if len(final_user_arr) ==1:
                        gs= GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_user_arr[0].first_name if final_user_arr[0].first_name else '-'),assgn_last_name=(final_user_arr[0].last_name if final_user_arr[0].last_name else '-'),smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="no",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                        gs.save()
                        return Response(GsReportFunnelSerializer(gs).data)
                    else:
                        gs= GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_group_arr[0].groupname if final_group_arr[0].groupname else '-'),assgn_last_name="group",smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="no",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                        gs.save()
                        return Response(GsReportFunnelSerializer(gs).data)
                elif len(add_list_ids) == 0:
                    gs= GsReportFunnel(leadid='0', city='-', state='-', pobox='-', country='-',phone='-',mobile='-',assgn_first_name='-',assgn_last_name='-',smownerid='0',description='-',createdtime='1992-01-01T12:00:00',modifiedtime='1992-01-01T12:00:00',lead_no='-',email='-',firstname='-',lastname='-',company='-',leadstatus='-',leadsource='-',course='-',campaign_id='-',google_keyword='-',ref_domain='-',traffic_src='-',google_cookie='-',verified="no",has_multiple_leads="no",payments_hdfc_id=(payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                    gs.save()
                    return Response(GsReportFunnelSerializer(gs).data)
                else:
                    if len(users_index)>0:
                        if 0 in users_index:
                            gs=GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_user_arr[0].first_name if final_user_arr[0].first_name else '-'),assgn_last_name=(final_user_arr[0].last_name if final_user_arr[0].last_name else '-'),smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                            gs.save()
                    if len(groups_index)>0:
                        if 0 in groups_index:
                            gs=GsReportFunnel(leadid=(final_det_arr[0].leadid if final_det_arr[0].leadid else '-'), city=(final_add_arr[0].city if final_add_arr[0].city else '-'), state=(final_add_arr[0].state if final_add_arr[0].state else '-'), pobox=(final_add_arr[0].pobox if final_add_arr[0].pobox else '-'), country=(final_add_arr[0].country if final_add_arr[0].country else '-'),phone=(final_add_arr[0].phone if final_add_arr[0].phone else '-'),mobile=(final_add_arr[0].mobile if final_add_arr[0].mobile else '-'),assgn_first_name=(final_group_arr[0].groupname if final_group_arr[0].groupname else '-'),assgn_last_name="Group",smownerid=( final_crm_entity_arr[0].smownerid if final_crm_entity_arr[0].smownerid else '-'),description=(final_crm_entity_arr[0].description if final_crm_entity_arr[0].description else '-'),createdtime=(final_crm_entity_arr[0].createdtime if final_crm_entity_arr[0].createdtime else '-'),modifiedtime=(final_crm_entity_arr[0].modifiedtime if final_crm_entity_arr[0].modifiedtime else '-'),lead_no=(final_det_arr[0].lead_no if final_det_arr[0].lead_no else '-'),email=(final_det_arr[0].email if final_det_arr[0].email else '-'),firstname=(final_det_arr[0].firstname if final_det_arr[0].firstname else '-'),lastname=(final_det_arr[0].lastname if final_det_arr[0].lastname else '-'),company=(final_det_arr[0].company if final_det_arr[0].company else '-'),leadstatus=(final_det_arr[0].leadstatus if final_det_arr[0].leadstatus else '-'),leadsource=(final_det_arr[0].leadsource if final_det_arr[0].leadsource else '-'),course=( final_cf_arr[0].cf_607 if final_cf_arr[0].cf_607 else '-'),campaign_id=(final_cf_arr[0].cf_609 if final_cf_arr[0].cf_609 else '-'),google_keyword=(final_cf_arr[0].cf_632 if final_cf_arr[0].cf_632 else '-'),ref_domain=(final_cf_arr[0].cf_633 if final_cf_arr[0].cf_633 else '-'),traffic_src=( final_cf_arr[0].cf_679 if final_cf_arr[0].cf_679 else '-'),google_cookie=(final_cf_arr[0].cf_689 if final_cf_arr[0].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-'))
                            gs.save()
                    for i in range(0, len(add_list_ids)):
                        if i in users_index:
                            GsReportFunnelMultiple(leadid=(final_det_arr[i].leadid if final_det_arr[i].leadid else '-'),gs_id= gs.id, city=(final_add_arr[i].city if final_add_arr[i].city else '-'), state=(final_add_arr[i].state if final_add_arr[i].state else '-'), pobox=(final_add_arr[i].pobox if final_add_arr[i].pobox else '-'), country=(final_add_arr[i].country if final_add_arr[i].country else '-'),phone=(final_add_arr[i].phone if final_add_arr[i].phone else '-'),mobile=(final_add_arr[i].mobile if final_add_arr[i].mobile else '-'),assgn_first_name=(final_user_arr[users_index.index(i)].first_name if final_user_arr[users_index.index(i)].first_name else '-'),assgn_last_name=(final_user_arr[users_index.index(i)].last_name if final_user_arr[users_index.index(i)].last_name else '-'),smownerid=( final_crm_entity_arr[i].smownerid if final_crm_entity_arr[i].smownerid else '-'),description=(final_crm_entity_arr[i].description if final_crm_entity_arr[i].description else '-'),createdtime=(final_crm_entity_arr[i].createdtime if final_crm_entity_arr[i].createdtime else '-'),modifiedtime=(final_crm_entity_arr[i].modifiedtime if final_crm_entity_arr[i].modifiedtime else '-'),lead_no=(final_det_arr[i].lead_no if final_det_arr[i].lead_no else '-'),email=(final_det_arr[i].email if final_det_arr[i].email else '-'),firstname=(final_det_arr[i].firstname if final_det_arr[i].firstname else '-'),lastname=(final_det_arr[i].lastname if final_det_arr[i].lastname else '-'),company=(final_det_arr[i].company if final_det_arr[i].company else '-'),leadstatus=(final_det_arr[i].leadstatus if final_det_arr[i].leadstatus else '-'),leadsource=(final_det_arr[i].leadsource if final_det_arr[i].leadsource else '-'),course=( final_cf_arr[i].cf_607 if final_cf_arr[i].cf_607 else '-'),campaign_id=(final_cf_arr[i].cf_609 if final_cf_arr[i].cf_609 else '-'),google_keyword=(final_cf_arr[i].cf_632 if final_cf_arr[i].cf_632 else '-'),ref_domain=(final_cf_arr[i].cf_633 if final_cf_arr[i].cf_633 else '-'),traffic_src=( final_cf_arr[i].cf_679 if final_cf_arr[i].cf_679 else '-'),google_cookie=(final_cf_arr[i].cf_689 if final_cf_arr[i].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-')).save()
                        else:
                            GsReportFunnelMultiple(leadid=(final_det_arr[i].leadid if final_det_arr[i].leadid else '-'),gs_id= gs.id, city=(final_add_arr[i].city if final_add_arr[i].city else '-'), state=(final_add_arr[i].state if final_add_arr[i].state else '-'), pobox=(final_add_arr[i].pobox if final_add_arr[i].pobox else '-'), country=(final_add_arr[i].country if final_add_arr[i].country else '-'),phone=(final_add_arr[i].phone if final_add_arr[i].phone else '-'),mobile=(final_add_arr[i].mobile if final_add_arr[i].mobile else '-'),assgn_first_name=(final_group_arr[groups_index.index(i)].groupname if final_group_arr[groups_index.index(i)].groupname else '-'),assgn_last_name="Group",smownerid=( final_crm_entity_arr[i].smownerid if final_crm_entity_arr[i].smownerid else '-'),description=(final_crm_entity_arr[i].description if final_crm_entity_arr[i].description else '-'),createdtime=(final_crm_entity_arr[i].createdtime if final_crm_entity_arr[i].createdtime else '-'),modifiedtime=(final_crm_entity_arr[i].modifiedtime if final_crm_entity_arr[i].modifiedtime else '-'),lead_no=(final_det_arr[i].lead_no if final_det_arr[i].lead_no else '-'),email=(final_det_arr[i].email if final_det_arr[i].email else '-'),firstname=(final_det_arr[i].firstname if final_det_arr[i].firstname else '-'),lastname=(final_det_arr[i].lastname if final_det_arr[i].lastname else '-'),company=(final_det_arr[i].company if final_det_arr[i].company else '-'),leadstatus=(final_det_arr[i].leadstatus if final_det_arr[i].leadstatus else '-'),leadsource=(final_det_arr[i].leadsource if final_det_arr[i].leadsource else '-'),course=( final_cf_arr[i].cf_607 if final_cf_arr[i].cf_607 else '-'),campaign_id=(final_cf_arr[i].cf_609 if final_cf_arr[i].cf_609 else '-'),google_keyword=(final_cf_arr[i].cf_632 if final_cf_arr[i].cf_632 else '-'),ref_domain=(final_cf_arr[i].cf_633 if final_cf_arr[i].cf_633 else '-'),traffic_src=( final_cf_arr[i].cf_679 if final_cf_arr[i].cf_679 else '-'),google_cookie=(final_cf_arr[i].cf_689 if final_cf_arr[i].cf_689 else '-'),verified="no",has_multiple_leads="yes",payments_hdfc_id= (payments_hdfc_id if payments_hdfc_id else 0),currency = (currency if currency else '-'),amount= (amount if amount else 0.0),payment_id = (payment_id if payment_id else '-'),result=(result if result else '-'),tran_id= (tran_id if tran_id else '-'),postdate=(postdate if postdate else '-'),details=(details if details else '-'),auth = (auth if auth else '-'),error = (error if error else '-'),error_msg = (error_msg if error_msg else '-'),udf1= (udf1 if udf1 else '-'),udf2= (udf2 if udf2 else '-'),udf3= (udf3 if udf3 else '-'),udf4= (udf4 if udf4 else '-'),udf5= (udf5 if udf5 else '-'),product_id=(product_id if product_id else 0),created=(created if created else '-'),source=(source if source else '-'),converted_amount=(converted_amount if converted_amount else '0'),region=(region if region else '-')).save()
                    return Response(GsReportFunnelSerializer(gs).data)

        else:
            return Response('{"error":"Not captured"}')

    def put(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = ReportSerializer(report, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GunshotList(APIView):
    """
    List all gunshot objects, or create a new gunshot object.
    """
    def get(self, request, format=None):
        email = request.GET.get('email', False)
        phone = request.GET.get('phone', False)
        if email:
            if phone:
                gs = GsReportFunnel.objects.filter(udf1= email, phone=phone)
            else:
                gs = GsReportFunnel.objects.filter(udf1= email)
        else:
            gs = GsReportFunnel.objects.all()
        
        serializer = GsReportFunnelSerializer(gs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GsReportFunnelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GunshotDetail(APIView):
    """
    Retrieve, update or delete a report instance.
    """
    def get_object(self, pk):
        try:
            return GsReportFunnel.objects.get(pk=pk)
        except GsReportFunnel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gs = self.get_object(pk)
        serializer = GsReportFunnelSerializer(gs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gs = self.get_object(pk)
        serializer = GsReportFunnelSerializer(gs, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gs = self.get_object(pk)
        gs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GunshotMultipleList(APIView):
    """
    List all gunshot multiple objects, or create a new gunshot object.
    """
    def get(self, request, format=None):
        email = request.GET.get('email', False)
        phone = request.GET.get('phone', False)
        if email:
            if phone:
                gs = GsReportFunnel.objects.filter(udf1= email, phone=phone)
            else:
                gs = GsReportFunnel.objects.filter(udf1= email)
        else:
            gs = GsReportFunnel.objects.all()

        gsm = GsReportFunnelMultiple.objects.filter(gs_id= gs[0].id)
        serializer = GsReportFunnelMultipleSerializer(gsm, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GsReportFunnelMultipleSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GunshotMultipleDetail(APIView):
    """
    Retrieve, update or delete a gunshot_multiple instance.
    """
    def get_object(self, pk):
        try:
            return GsReportFunnelMultiple.objects.filter(gs_id=pk)
        except GsReportFunnel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gs = self.get_object(pk)
        serializer = GsReportFunnelMultipleSerializer(gs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gs = self.get_object(pk)
        serializer = GsReportFunnelMultipleSerializer(gs, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gs = self.get_object(pk)
        gs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SalesReport(APIView):
    
    def get(self, request, format=None):
        if request.session.get('user_id', False):
            now = datetime.datetime.now()
            name="Aayush"
            #Truncations
            truncate_date_yearly = connection.ops.date_trunc_sql('year','created')
            truncate_date_monthly = connection.ops.date_trunc_sql('month','created')
            truncate_date_daily = connection.ops.date_trunc_sql('day','created')
            named_grouped_yearly= []
            named_grouped_monthly= []
            named_grouped_daily=[]

            gs_objects = GsReportFunnel.objects.all()[0:10]

            #All time data grouped by Assgn_First_Name
            data=GsReportFunnel.objects.exclude(assgn_last_name = "Group").values('assgn_first_name').annotate(sales=Sum('amount'))
            
            #Total Yearly Data
            gs = GsReportFunnel.objects.extra({'year':truncate_date_yearly})
            yearly = gs.values('year').annotate(Sum('amount'), Count('pk')).order_by('year')
       
            #Total Monthly Data
            gs = GsReportFunnel.objects.extra({'month':truncate_date_monthly})
            monthly = gs.values('month').annotate(Sum('amount'), Count('pk')).order_by('month')   

            #Total Daily Data
            gs = GsReportFunnel.objects.extra({'day':truncate_date_daily})
            daily = gs.values('day').annotate(Sum('amount'), Count('pk')).order_by('day')

            #Grouped Yearly,Monthly,Daily Data
            for d in data:
                grouped_obj = GsReportFunnel.objects.filter(assgn_first_name = d['assgn_first_name'])
                
                grouped_yearly= []
                gs_y= grouped_obj.extra({'year':truncate_date_yearly})
                yearly_grouped = gs_y.values('year').annotate(Sum('amount'), Count('pk')).order_by('year')
                grouped_yearly.append(yearly_grouped)
                named_grouped_yearly.append({'assgn_first_name':d['assgn_first_name'],'total_sales':d['sales'],'grouped_yearly':grouped_yearly})
                
                grouped_monthly= []
                gs_m= grouped_obj.extra({'month':truncate_date_monthly})
                monthly_grouped = gs_m.values('month').annotate(Sum('amount'), Count('pk')).order_by('month')
                grouped_monthly.append(monthly_grouped)
                named_grouped_monthly.append({'assgn_first_name':d['assgn_first_name'],'total_sales':d['sales'],'grouped_monthly':grouped_monthly})
                
                grouped_daily=[]
                gs_d= grouped_obj.extra({'day':truncate_date_daily})
                daily_grouped = gs_d.values('day').annotate(Sum('amount'), Count('pk')).order_by('day')
                grouped_daily.append(daily_grouped)
                named_grouped_daily.append({'assgn_first_name':d['assgn_first_name'],'total_sales':d['sales'],'grouped_daily':grouped_daily})
            
            # Get unique months, years, days for graphs
            unique_years= []
            for gy in named_grouped_yearly:
                for y in gy['grouped_yearly'][0]:
                    year = str(y['year'].year)
                    unique_years.append(year)
            unique_years= list(reversed(sorted(list(set(unique_years)))))
            
            unique_months= []
            for gm in named_grouped_monthly:
                for m in gm['grouped_monthly'][0]:
                    month = str(m['month'].month)+'/'+str(m['month'].year)
                    unique_months.append(month)
            unique_months= list(set(unique_months))
            unique_months=list(reversed(sorted(unique_months, key=lambda x: datetime.datetime.strptime(x, '%m/%Y'))))

            
            unique_days= []
            for gd in named_grouped_daily:
                for d in gd['grouped_daily'][0]:
                    day = str(d['day'].day)+'/'+str(d['day'].month)+'/'+str(d['day'].year)
                    unique_days.append(day)
            unique_days= list(set(unique_days))
            unique_days=list(reversed(sorted(unique_days, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))))
            
            final_yearly =[]
            for gy in named_grouped_yearly:
                yearly_data = []
                for uy in unique_years:
                    flag = False
                    for y in gy['grouped_yearly'][0]:
                        if str(y['year'].year) == uy:
                            yearly_data.append({"year": uy,"amount": y['amount__sum']})
                            flag = True
                    if flag == False :
                        yearly_data.append({"year": uy,"amount": "0"})
                fy = {'assgn_first_name':gy['assgn_first_name'], 'total_sales':gy['total_sales'], 'yearly_data': yearly_data}
                final_yearly.append(fy)    
            named_grouped_yearly = final_yearly

            final_monthly =[]
            for gm in named_grouped_monthly:
                monthly_data = []
                for um in unique_months:
                    flag = False
                    for m in gm['grouped_monthly'][0]:
                        if str(m['month'].month)+'/'+str(m['month'].year) == um:
                            monthly_data.append({"month": um,"amount": m['amount__sum']})
                            flag = True
                    if flag == False :
                        monthly_data.append({"month": um,"amount": "0"})
                fm = {'assgn_first_name':gm['assgn_first_name'], 'total_sales':gm['total_sales'], 'monthly_data': monthly_data}
                final_monthly.append(fm)    
            named_grouped_monthly = final_monthly

            final_daily =[]
            for gd in named_grouped_daily:
                daily_data = []
                for ud in unique_days:
                    flag = False
                    for d in gd['grouped_daily'][0]:
                        if str(d['day'].day)+'/'+str(d['day'].month)+'/'+str(d['day'].year) == ud:
                            daily_data.append({"day": ud,"amount": d['amount__sum']})
                            flag = True
                    if flag == False :
                        daily_data.append({"day": ud,"amount": "0"})
                fd = {'assgn_first_name':gd['assgn_first_name'], 'total_sales':gd['total_sales'], 'daily_data': daily_data}
                final_daily.append(fd)    
            named_grouped_daily = final_daily

            bar_series =[]
            for d in named_grouped_monthly[0:10]:
                temp_data=[]
                for um in unique_months[0:5]:
                    for m in d['monthly_data']:
                        if m['month'] == um:
                            temp_data.append(float(m['amount']))
                temp ={'name': d['assgn_first_name'].encode("utf-8"), 'data': temp_data }
                bar_series.append(temp)
            bar_categories= unique_months[0:5]

            pie_data=[]
            temp_total = 0
            for d in named_grouped_yearly[0:10]:
                temp_total += d['total_sales']

            for d in named_grouped_yearly[0:10]:
                temp = []
                temp.append(d['assgn_first_name'].encode("utf-8"))
                temp.append(float(d['total_sales'])/temp_total*100)
                pie_data.append(temp)

            monthly_max = {'month':str(max(monthly)['month'].month)+'/'+str(max(monthly)['month'].year),'amount': str(max(monthly)['amount__sum'])}
            return render(request, 'sales_report.html', {'root_url':settings.ROOT_URL,'monthly_max':monthly_max,'gs_objects': gs_objects,'pie_data': pie_data,'bar_categories': bar_categories,'bar_series':bar_series,'unique_years':unique_years,'unique_months':unique_months,'unique_days':unique_days,'current_date': now, 'name':name,'data':data,'monthly': monthly,'yearly': yearly,'daily': daily,'named_grouped_yearly':named_grouped_yearly,'named_grouped_monthly':named_grouped_monthly,'named_grouped_daily':named_grouped_daily})

        else:
            return redirect('/login')
class PrintReport(APIView):
    
    def get(self, request, format=None):
        link=request.GET.get('link', False)
        name=request.GET.get('name', False)
        link= settings.ROOT_URL+'sales_report/'
        name='Sales Report'
        pdfkit.from_url(link, 'static/user_data/reports/'+name+'.pdf')
        now = datetime.datetime.now()
        return redirect('../static/user_data/reports/'+name+'.pdf')

class MailReport(APIView):
    
    def get(self, request, format=None):
        email = EmailMessage('Test subject', 'This is the body', 'manish@edupristine.org',['jainaayush05@gmail.com'],headers = {'Reply-To': 'manish@edupristine.org'})
        email.attach_file('static/user_data/reports/sales_report.pdf')
        email.send("fail_silently=False")
        return redirect('../static/user_data/reports/Sales Report.pdf')

class FunnelReport(APIView):
    
    def get(self, request, format=None):
        if request.session.get('user_id', False):
            labels = GsFunnelLabel.objects.filter(parent = 0).order_by('display_order')
            funnel_data= []
            for l in labels:
                so= GsFunnelLabel.objects.filter(parent = l.id).order_by('display_order')
                lo_data=[]
                for o in so:
                    data = GsFunnelDataMonthly.objects.filter(metric_id = o.id)
                    so_data=[]
                    for d in data:
                        so_data.append({"month":d.date , "value": d.value })
                    lo_data.append({"sublabel":o.label, "data": so_data})

                sl = {"label": l.label,"sublabels":lo_data}
                funnel_data.append(sl)

            return render(request, 'funnel_report.html', {"funnel_data": funnel_data})
        else:
            return redirect('/login')

    def post(self, request, format=None):
        label= request.POST.get('funnel_data_label', False)
        date = request.POST.get('funnel_data_'+label+'_month', False)
        
        label_obj =GsFunnelLabel.objects.get(label= label, parent=0)
        
        sublabel_objs = GsFunnelLabel.objects.filter(parent=label_obj.id)
        gsd=""
        i=1
        for sublabel_obj in sublabel_objs:
            sublabel= request.POST.get('funnel_data_'+label+'_sublabel'+str(i), False)
            value= request.POST.get('funnel_data_'+label+'_value'+str(i), False)
            if value:
                value = 0
                
            sl = GsFunnelLabel.objects.get(label = sublabel, parent=label_obj.id)
            gsd =GsFunnelDataMonthly(metric_id = sl.id, value= value, date= date)
            gsd.save()
            i +=1

        return Response("done")
