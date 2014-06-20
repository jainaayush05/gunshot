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