from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class GsReportFunnel(models.Model):
    leadid = models.IntegerField() #
    city = models.CharField(max_length=30, blank=True,null=True) #
    state = models.CharField(max_length=30, blank=True) #
    pobox = models.CharField(max_length=30, blank=True) #
    country = models.CharField(max_length=30, blank=True) #
    phone = models.CharField(max_length=50, blank=True) #
    mobile = models.CharField(max_length=50, blank=True) #
    assgn_first_name = models.CharField(max_length=30, blank=True) #
    assgn_last_name = models.CharField(max_length=30, blank=True) #
    smownerid = models.IntegerField(blank=True) #
    description = models.TextField(blank=True) #
    createdtime = models.DateTimeField(blank=True) #
    modifiedtime = models.DateTimeField(blank=True) #
    lead_no = models.CharField(max_length=100, blank=True) #
    email = models.CharField(max_length=100, blank=True) #
    firstname = models.CharField(max_length=40, blank=True) #
    lastname = models.CharField(max_length=80, blank=True) #
    company = models.CharField(max_length=100, blank=True) #
    leadstatus = models.CharField(max_length=50, blank=True) #
    leadsource = models.CharField(max_length=200, blank=True) #
    course = models.CharField(max_length=25, blank=True) #Course
    campaign_id = models.CharField(max_length=10, blank=True) #Campaign_ID
    google_keyword = models.CharField(max_length=150, blank=True) #Google_Keyword
    ref_domain = models.CharField(max_length=255, blank=True) #Referring Domain
    traffic_src = models.CharField(max_length=256, blank=True) # Traffic source
    google_cookie = models.CharField(max_length=255, blank=True) # Google Cookie
    verified = models.CharField(max_length=255, blank=True) # Verification
    has_multiple_leads = models.CharField(max_length=255, blank=True)
    payments_hdfc_id = models.IntegerField(blank=True)
    currency = models.CharField(max_length=10)
    amount = models.FloatField()
    payment_id = models.CharField(max_length=50)
    result = models.CharField(max_length=50, blank=True)
    tran_id = models.CharField(max_length=50, blank=True)
    postdate = models.CharField(max_length=20, blank=True)
    details = models.CharField(max_length=250, blank=True)
    auth = models.CharField(max_length=50, blank=True)
    error = models.CharField(max_length=50, blank=True)
    error_msg = models.CharField(max_length=250, blank=True)
    udf1 = models.CharField(max_length=256, blank=True)
    udf2 = models.CharField(max_length=512, blank=True)
    udf3 = models.CharField(max_length=256, blank=True)
    udf4 = models.CharField(max_length=256, blank=True)
    udf5 = models.CharField(max_length=256, blank=True)
    product_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    source = models.CharField(max_length=21, blank=True)
    converted_amount = models.FloatField(blank=True)
    region = models.CharField(max_length=256, blank=True)

    #@classmethod
    #def create(cls,leadid,city,state,pobox,country,phone,mobile,assgn_first_name,assgn_last_name,smownerid,description,createdtime,modifiedtime,lead_no,email,firstname,lastname,company,leadstatus,leadsource,course,campaign_id,google_keyword,ref_domain,traffic_src,google_cookie,verified,has_multiple_leads):
    #    GsReportFunnel = cls(leadid=leadid,city=city,state=state,pobox=pobox,country=country,phone=phone,mobile=mobile,assgn_first_name=assgn_first_name,assgn_last_name=assgn_last_name,smownerid=smownerid,description=description,createdtime=createdtime,modifiedtime=modifiedtime,lead_no=lead_no,email=email,firstname=firstname,lastname=lastname,company=company,leadstatus=leadstatus,leadsource=leadsource,course=course,campaign_id=campaign_id,google_keyword=google_keyword,ref_domain=ref_domain,traffic_src=traffic_src,google_cookie=google_cookie,verified=verified, has_multiple_leads=has_multiple_leads)
    #    # do something with the book
    #    return GsReportFunnel
    
    class Meta:
        managed = True
        db_table = 'gs_report_funnel'

class GsReportFunnelMultiple(models.Model):
    gs_id = models.IntegerField() #
    leadid = models.IntegerField() #
    city = models.CharField(max_length=30, blank=True,null=True) #
    state = models.CharField(max_length=30, blank=True) #
    pobox = models.CharField(max_length=30, blank=True) #
    country = models.CharField(max_length=30, blank=True) #
    phone = models.CharField(max_length=50, blank=True) #
    mobile = models.CharField(max_length=50, blank=True) #
    assgn_first_name = models.CharField(max_length=30, blank=True) #
    assgn_last_name = models.CharField(max_length=30, blank=True) #
    smownerid = models.IntegerField(blank=True) #
    description = models.TextField(blank=True) #
    createdtime = models.DateTimeField(blank=True) #
    modifiedtime = models.DateTimeField(blank=True) #
    lead_no = models.CharField(max_length=100, blank=True) #
    email = models.CharField(max_length=100, blank=True) #
    firstname = models.CharField(max_length=40, blank=True) #
    lastname = models.CharField(max_length=80, blank=True) #
    company = models.CharField(max_length=100, blank=True) #
    leadstatus = models.CharField(max_length=50, blank=True) #
    leadsource = models.CharField(max_length=200, blank=True) #
    course = models.CharField(max_length=25, blank=True) #Course
    campaign_id = models.CharField(max_length=10, blank=True) #Campaign_ID
    google_keyword = models.CharField(max_length=150, blank=True) #Google_Keyword
    ref_domain = models.CharField(max_length=255, blank=True) #Referring Domain
    traffic_src = models.CharField(max_length=256, blank=True) # Traffic source
    google_cookie = models.CharField(max_length=255, blank=True) # Google Cookie
    verified = models.CharField(max_length=255, blank=True) # Verification
    has_multiple_leads = models.CharField(max_length=255, blank=True)
    payments_hdfc_id = models.IntegerField(blank=True)
    currency = models.CharField(max_length=10)
    amount = models.FloatField()
    payment_id = models.CharField(max_length=50)
    result = models.CharField(max_length=50, blank=True)
    tran_id = models.CharField(max_length=50, blank=True)
    postdate = models.CharField(max_length=20, blank=True)
    details = models.CharField(max_length=250, blank=True)
    auth = models.CharField(max_length=50, blank=True)
    error = models.CharField(max_length=50, blank=True)
    error_msg = models.CharField(max_length=250, blank=True)
    udf1 = models.CharField(max_length=256, blank=True)
    udf2 = models.CharField(max_length=512, blank=True)
    udf3 = models.CharField(max_length=256, blank=True)
    udf4 = models.CharField(max_length=256, blank=True)
    udf5 = models.CharField(max_length=256, blank=True)
    product_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    source = models.CharField(max_length=21, blank=True)
    converted_amount = models.FloatField(blank=True)
    region = models.CharField(max_length=256, blank=True)
    #@classmethod
    #def create(cls,leadid,city,state,pobox,country,phone,mobile,assgn_first_name,assgn_last_name,smownerid,description,createdtime,modifiedtime,lead_no,email,firstname,lastname,company,leadstatus,leadsource,course,campaign_id,google_keyword,ref_domain,traffic_src,google_cookie,verified,has_multiple_leads):
    #    GsReportFunnel = cls(leadid=leadid,city=city,state=state,pobox=pobox,country=country,phone=phone,mobile=mobile,assgn_first_name=assgn_first_name,assgn_last_name=assgn_last_name,smownerid=smownerid,description=description,createdtime=createdtime,modifiedtime=modifiedtime,lead_no=lead_no,email=email,firstname=firstname,lastname=lastname,company=company,leadstatus=leadstatus,leadsource=leadsource,course=course,campaign_id=campaign_id,google_keyword=google_keyword,ref_domain=ref_domain,traffic_src=traffic_src,google_cookie=google_cookie,verified=verified, has_multiple_leads=has_multiple_leads)
    #    # do something with the book
    #    return GsReportFunnel
    
    class Meta:
        managed = True
        db_table = 'gs_report_funnel_multiple'