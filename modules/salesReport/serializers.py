from django.forms import widgets 
from rest_framework import serializers
from modules.funnelReport.models import GsFunnelDataMonthly,GsFunnelLabel, LANGUAGE_CHOICES, STYLE_CHOICES
from modules.salesReport.models import GsReportFunnel,GsReportFunnelMultiple
from modules.vtigerCrm.models import VtigerGroups,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf


class GsReportFunnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsReportFunnel
        fields = ('id', 'leadid', 'city', 'state', 'pobox', 'country','phone','mobile','assgn_first_name','assgn_last_name','smownerid','description','createdtime','modifiedtime','lead_no','email','firstname','lastname','company','leadstatus','leadsource','course','campaign_id','google_keyword','ref_domain','traffic_src','google_cookie','verified','has_multiple_leads','payments_hdfc_id','currency','amount','payment_id','result','tran_id','postdate','details','auth','error','error_msg','udf1','udf2','udf3','udf4','udf5','product_id','created','source') 

class GsReportFunnelMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsReportFunnelMultiple
        fields = ('id','gs_id', 'leadid', 'city', 'state', 'pobox', 'country','phone','mobile','assgn_first_name','assgn_last_name','smownerid','description','createdtime','modifiedtime','lead_no','email','firstname','lastname','company','leadstatus','leadsource','course','campaign_id','google_keyword','ref_domain','traffic_src','google_cookie','verified','has_multiple_leads','payments_hdfc_id','currency','amount','payment_id','result','tran_id','postdate','details','auth','error','error_msg','udf1','udf2','udf3','udf4','udf5','product_id','created','source') 
