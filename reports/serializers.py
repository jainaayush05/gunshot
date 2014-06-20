from django.forms import widgets 
from rest_framework import serializers
from module.funnelReport.models import GsFunnelDataMonthly,GsFunnelLabel, LANGUAGE_CHOICES, STYLE_CHOICES
from module.salesReport.models import GsReportFunnel,GsReportFunnelMultiple
from module.vtigerCrm.models import VtigerGroups,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

