from modules.funnelReport.models import GsFunnelDataMonthly,GsFunnelLabel
from modules.salesReport.models import GsReportFunnel,GsReportFunnelMultiple
from modules.vtigerCrm.models import VtigerGroups,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf
from modules.funnelReport.serializers import GsFunnelDataMonthlySerializer,GsFunnelLabelSerializer
from modules.salesReport.serializers import GsReportFunnelSerializer,GsReportFunnelMultipleSerializer
from modules.vtigerCrm.serializers import VtigerGroupsSerializer,VtigerLeaddetailsSerializer,VtigerLeadaddressSerializer,VtigerCrmentitySerializer
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


class CreateLead(APIView):
    """
    Create a lead in VTigerCRM
    """

    def post(self, request, format=None):
        ##Push Lead
        data =request.POST.get('lead_data', False)
        email =request.POST.get('email', False)
        url =settings.CRM_URL+'moduless/Webforms/post.php/'
        http_headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}
        req = urllib2.Request(url, data, http_headers)
        #import ipdb;ipdb.set_trace();
        response = urllib2.urlopen(req)

        ##Get Lead Number
        url =settings.CRM_URL+'moduless/harry/post.php/'
        data = "getlead=1&email="+email
        req = urllib2.Request(url, data, http_headers)
        lead_no = urllib2.urlopen(req).read()

        ##Create Account
        data =request.POST.get('account_data', False)
        data=data+lead_no
        url =settings.CRM_URL+'moduless/Webforms/post.php/'
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
            url =settings.CRM_URL+'moduless/harry/post.php/'
            data = "lead_no="+lead_no+"&assign="+user.user_name
            req = urllib2.Request(url, data, http_headers)
            response = urllib2.urlopen(req).read()
            gs= GsReportFunnel.objects.get(id= gs_id)
            gs.assgn_first_name= user.first_name
            gs.save()
        
        return Response(response)

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
