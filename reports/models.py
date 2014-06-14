from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)

    class Meta:
        ordering = ('created',)
        
class GsFunnelFormula(models.Model):
    belongs_to = models.IntegerField(blank=True)
    f1 = models.IntegerField(blank=True)
    f2 = models.IntegerField(blank=True)
    type = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'gs_funnel_formula'

class GsFunnelLabel(models.Model):
    label = models.CharField(max_length=255, blank=True)
    parent = models.IntegerField(blank=True)
    type = models.CharField(max_length=255, blank=True)
    group_source_type = models.CharField(max_length=255, blank=True)
    display_order = models.IntegerField(blank=True) #

    class Meta:
        managed = True
        db_table = 'gs_funnel_label'

class GsFunnelDataMonthly(models.Model):
    metric_id = models.IntegerField(blank=True)
    value = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True)
    
    class Meta:
        managed = True
        db_table = 'gs_funnel_data_monthly'

class VtigerUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True)
    user_password = models.CharField(max_length=200, blank=True)
    user_hash = models.CharField(max_length=32, blank=True)
    cal_color = models.CharField(max_length=25, blank=True)
    first_name = models.CharField(max_length=30, blank=True) #
    last_name = models.CharField(max_length=30, blank=True) #
    reports_to_id = models.CharField(max_length=36, blank=True)
    is_admin = models.CharField(max_length=3, blank=True)
    currency_id = models.IntegerField()
    description = models.TextField(blank=True)
    date_entered = models.DateTimeField()
    date_modified = models.DateTimeField()
    modified_user_id = models.CharField(max_length=36, blank=True)
    title = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    phone_home = models.CharField(max_length=50, blank=True)
    phone_mobile = models.CharField(max_length=50, blank=True)
    phone_work = models.CharField(max_length=50, blank=True)
    phone_other = models.CharField(max_length=50, blank=True)
    phone_fax = models.CharField(max_length=50, blank=True)
    email1 = models.CharField(max_length=100, blank=True)
    email2 = models.CharField(max_length=100, blank=True)
    secondaryemail = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=25, blank=True)
    signature = models.CharField(max_length=1000, blank=True)
    address_street = models.CharField(max_length=150, blank=True)
    address_city = models.CharField(max_length=100, blank=True)
    address_state = models.CharField(max_length=100, blank=True)
    address_country = models.CharField(max_length=25, blank=True)
    address_postalcode = models.CharField(max_length=9, blank=True)
    user_preferences = models.TextField(blank=True)
    tz = models.CharField(max_length=30, blank=True)
    holidays = models.CharField(max_length=60, blank=True)
    namedays = models.CharField(max_length=60, blank=True)
    workdays = models.CharField(max_length=30, blank=True)
    weekstart = models.IntegerField(blank=True, null=True)
    date_format = models.CharField(max_length=200, blank=True)
    hour_format = models.CharField(max_length=30, blank=True)
    start_hour = models.CharField(max_length=30, blank=True)
    end_hour = models.CharField(max_length=30, blank=True)
    activity_view = models.CharField(max_length=200, blank=True)
    lead_view = models.CharField(max_length=200, blank=True)
    imagename = models.CharField(max_length=250, blank=True)
    deleted = models.IntegerField()
    confirm_password = models.CharField(max_length=200, blank=True)
    internal_mailer = models.CharField(max_length=3)
    reminder_interval = models.CharField(max_length=100, blank=True)
    reminder_next_time = models.CharField(max_length=100, blank=True)
    crypt_type = models.CharField(max_length=20)
    accesskey = models.CharField(max_length=36, blank=True)
    theme = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=36, blank=True)
    time_zone = models.CharField(max_length=200, blank=True)
    currency_grouping_pattern = models.CharField(max_length=100, blank=True)
    currency_decimal_separator = models.CharField(max_length=2, blank=True)
    currency_grouping_separator = models.CharField(max_length=2, blank=True)
    currency_symbol_placement = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_users'


class VtigerCrmentity(models.Model):
    crmid = models.IntegerField(primary_key=True)
    smcreatorid = models.IntegerField()
    smownerid = models.IntegerField() #
    modifiedby = models.IntegerField()
    setype = models.CharField(max_length=30)
    description = models.TextField(blank=True) #
    createdtime = models.DateTimeField() #
    modifiedtime = models.DateTimeField() #
    viewedtime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True)
    version = models.IntegerField()
    presence = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_crmentity'

class VtigerLeaddetails(models.Model):
    leadid = models.IntegerField(primary_key=True) #
    lead_no = models.CharField(max_length=100) #
    email = models.CharField(max_length=100, blank=True) #
    interest = models.CharField(max_length=50, blank=True)
    firstname = models.CharField(max_length=40, blank=True) #
    salutation = models.CharField(max_length=200, blank=True) 
    lastname = models.CharField(max_length=80) #
    company = models.CharField(max_length=100) #
    annualrevenue = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True)
    campaign = models.CharField(max_length=30, blank=True)
    rating = models.CharField(max_length=200, blank=True)
    leadstatus = models.CharField(max_length=50, blank=True) #
    leadsource = models.CharField(max_length=200, blank=True) #
    converted = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True)
    licencekeystatus = models.CharField(max_length=50, blank=True)
    space = models.CharField(max_length=250, blank=True)
    comments = models.TextField(blank=True)
    priority = models.CharField(max_length=50, blank=True)
    demorequest = models.CharField(max_length=50, blank=True)
    partnercontact = models.CharField(max_length=50, blank=True)
    productversion = models.CharField(max_length=20, blank=True)
    product = models.CharField(max_length=50, blank=True)
    maildate = models.DateField(blank=True, null=True)
    nextstepdate = models.DateField(blank=True, null=True)
    fundingsituation = models.CharField(max_length=50, blank=True)
    purpose = models.CharField(max_length=50, blank=True)
    evaluationstatus = models.CharField(max_length=50, blank=True)
    transferdate = models.DateField(blank=True, null=True)
    revenuetype = models.CharField(max_length=50, blank=True)
    noofemployees = models.IntegerField(blank=True, null=True)
    secondaryemail = models.CharField(max_length=100, blank=True)
    assignleadchk = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'vtiger_leaddetails'

class VtigerLeadaddress(models.Model):
    leadaddressid = models.IntegerField(primary_key=True) #
    city = models.CharField(max_length=30, blank=True) #
    code = models.CharField(max_length=30, blank=True) 
    state = models.CharField(max_length=30, blank=True) #
    pobox = models.CharField(max_length=30, blank=True) #
    country = models.CharField(max_length=30, blank=True) #
    phone = models.CharField(max_length=50, blank=True) #
    mobile = models.CharField(max_length=50, blank=True) #
    fax = models.CharField(max_length=50, blank=True)
    lane = models.CharField(max_length=250, blank=True)
    leadaddresstype = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = True
        db_table = 'vtiger_leadaddress'

class VtigerLeadscf(models.Model):
    leadid = models.IntegerField(primary_key=True) #
    cf_607 = models.CharField(max_length=25, blank=True) #Course
    cf_609 = models.CharField(max_length=10, blank=True) #Campaign_ID
    cf_625 = models.DateField(blank=True, null=True)
    cf_630 = models.CharField(max_length=25, blank=True)
    cf_632 = models.CharField(max_length=150, blank=True) #Google_Keyword
    cf_633 = models.CharField(max_length=255, blank=True) #Referring Domain
    cf_634 = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    cf_636 = models.DateField(blank=True, null=True)
    cf_637 = models.CharField(max_length=255, blank=True)
    cf_638 = models.TextField(blank=True)
    cf_639 = models.TextField(blank=True)
    cf_640 = models.TextField(blank=True)
    cf_677 = models.TextField(blank=True)
    cf_678 = models.CharField(max_length=25, blank=True)
    cf_679 = models.CharField(max_length=256, blank=True) # Traffic source
    cf_689 = models.CharField(max_length=255, blank=True) # Google Cookie
    cf_690 = models.CharField(max_length=255, blank=True)
    cf_691 = models.CharField(max_length=255, blank=True)
    cf_694 = models.CharField(max_length=50, blank=True)
    cf_696 = models.CharField(max_length=20, blank=True)
    cf_704 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    cf_706 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    cf_707 = models.CharField(max_length=255, blank=True)
    cf_708 = models.CharField(max_length=255, blank=True)
    cf_709 = models.CharField(max_length=255, blank=True)
    cf_710 = models.CharField(max_length=255, blank=True)
    cf_711 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    cf_712 = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    cf_721 = models.TextField(blank=True)
    cf_722 = models.TextField(blank=True)
    cf_723 = models.TextField(blank=True)
    cf_724 = models.CharField(max_length=255, blank=True)
    cf_725 = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cf_727 = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cf_729 = models.CharField(max_length=255, blank=True)
    cf_733 = models.CharField(max_length=255, blank=True) #region
    class Meta:
        managed = True
        db_table = 'vtiger_leadscf'

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

class VtigerGroups(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(unique=True, max_length=100, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = True
        db_table = 'vtiger_groups'

