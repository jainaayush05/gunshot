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

class MailReport(APIView):
    
    def post(self, request, format=None):
        name=request.POST.get('name', False)
        to_email=request.POST.get('to_email', False)
        subject=request.POST.get('subject', False)
        link= settings.ROOT_URL+'sales_report/?print=true'
        now = datetime.datetime.now().strftime("_%Y-%m-%d_%H:%M:%S")
        name=name+now
        pdfkit.from_url(link, 'static/user_data/reports/'+name+'.pdf')
        email = EmailMessage(subject, 'pfa, sales report generated on '+now, 'manish@edupristine.org',[to_email],headers = {'Reply-To': 'manish@edupristine.org'})
        email.attach_file('static/user_data/reports/'+name+'.pdf')
        email.send("fail_silently=False")
        return Response('Mail successfully sent')