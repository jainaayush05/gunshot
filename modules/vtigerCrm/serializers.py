from django.forms import widgets 
from rest_framework import serializers
from modules.funnelReport.models import GsFunnelDataMonthly,GsFunnelLabel, LANGUAGE_CHOICES, STYLE_CHOICES
from modules.salesReport.models import GsReportFunnel,GsReportFunnelMultiple
from modules.vtigerCrm.models import VtigerGroups,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf


class VtigerLeadaddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VtigerLeadaddress
        fields = ('leadaddressid', 'city', 'code', 'state', 'pobox', 'country','phone','mobile','fax','lane','leadaddresstype')

class VtigerLeaddetailsSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = VtigerLeaddetails
        fields = ('leadid', 'lead_no', 'email', 'interest', 'firstname', 'salutation','lastname','company','annualrevenue','industry','campaign','rating','leadstatus','leadsource','converted','designation','licencekeystatus','space','comments','priority','demorequest','partnercontact','productversion','product','maildate','nextstepdate','fundingsituation','purpose','evaluationstatus','transferdate','revenuetype','noofemployees','secondaryemail','assignleadchk','address')
    address = VtigerLeadaddressSerializer()

class VtigerCrmentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VtigerCrmentity
        fields = ('crmid', 'smcreatorid', 'smownerid', 'modifiedby', 'setype', 'description','createdtime','modifiedtime','viewedtime','status','version','presence','deleted')

class VtigerGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VtigerGroups
        fields = ('groupid','groupname','description')
