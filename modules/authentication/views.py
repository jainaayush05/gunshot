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

def encryptPassword(nameStr, passStr):
        salt = nameStr[0:2]
        salt = '$1$' + salt.ljust(9,'0')
        return crypt.crypt(passStr, salt)


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