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