from django.forms import widgets 
from rest_framework import serializers
from reports.models import GsFunnelDataMonthly,Report,GsFunnelLabel,GsReportFunnelMultiple,VtigerGroups,GsReportFunnel,VtigerLeadscf,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, LANGUAGE_CHOICES, STYLE_CHOICES


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class GsFunnelLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsFunnelLabel
        fields = ('id', 'label', 'parent', 'type', 'group_source_type', 'display_order')

class GsFunnelDataMonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = GsFunnelDataMonthly
        fields = ('id', 'metric_id', 'value', 'date')

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

class GsReportFunnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsReportFunnel
        fields = ('id', 'leadid', 'city', 'state', 'pobox', 'country','phone','mobile','assgn_first_name','assgn_last_name','smownerid','description','createdtime','modifiedtime','lead_no','email','firstname','lastname','company','leadstatus','leadsource','course','campaign_id','google_keyword','ref_domain','traffic_src','google_cookie','verified','has_multiple_leads','payments_hdfc_id','currency','amount','payment_id','result','tran_id','postdate','details','auth','error','error_msg','udf1','udf2','udf3','udf4','udf5','product_id','created','source') 

class GsReportFunnelMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsReportFunnelMultiple
        fields = ('id','gs_id', 'leadid', 'city', 'state', 'pobox', 'country','phone','mobile','assgn_first_name','assgn_last_name','smownerid','description','createdtime','modifiedtime','lead_no','email','firstname','lastname','company','leadstatus','leadsource','course','campaign_id','google_keyword','ref_domain','traffic_src','google_cookie','verified','has_multiple_leads','payments_hdfc_id','currency','amount','payment_id','result','tran_id','postdate','details','auth','error','error_msg','udf1','udf2','udf3','udf4','udf5','product_id','created','source') 

class VtigerGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VtigerGroups
        fields = ('groupid','groupname','description')