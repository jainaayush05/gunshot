from django.forms import widgets 
from rest_framework import serializers
from modules.funnelReport.models import GsFunnelDataMonthly,GsFunnelLabel, LANGUAGE_CHOICES, STYLE_CHOICES
from modules.salesReport.models import GsReportFunnel,GsReportFunnelMultiple
from modules.vtigerCrm.models import VtigerGroups,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf


class GsFunnelLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsFunnelLabel
        fields = ('id', 'label', 'parent', 'type', 'group_source_type', 'display_order')

class GsFunnelDataMonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = GsFunnelDataMonthly
        fields = ('id', 'metric_id', 'value', 'date')