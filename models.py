# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class ComVtigerWorkflowActivatedonce(models.Model):
    workflow_id = models.IntegerField()
    entity_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflow_activatedonce'

class ComVtigerWorkflows(models.Model):
    workflow_id = models.IntegerField(unique=True)
    module_name = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=400)
    test = models.TextField(blank=True)
    execution_condition = models.IntegerField()
    defaultworkflow = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflows'

class ComVtigerWorkflowsSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflows_seq'

class ComVtigerWorkflowtaskQueue(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    entity_id = models.CharField(max_length=100, blank=True)
    do_after = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtask_queue'

class ComVtigerWorkflowtasks(models.Model):
    task_id = models.IntegerField(unique=True)
    workflow_id = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=400)
    task = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtasks'

class ComVtigerWorkflowtasksEntitymethod(models.Model):
    workflowtasks_entitymethod_id = models.IntegerField(unique=True)
    module_name = models.CharField(max_length=100, blank=True)
    method_name = models.CharField(max_length=100, blank=True)
    function_path = models.CharField(max_length=400, blank=True)
    function_name = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtasks_entitymethod'

class ComVtigerWorkflowtasksEntitymethodSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtasks_entitymethod_seq'

class ComVtigerWorkflowtasksSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtasks_seq'

class ComVtigerWorkflowtemplates(models.Model):
    template_id = models.IntegerField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=400, blank=True)
    template = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtemplates'

class ComVtigerWorkflowtemplatesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'com_vtiger_workflowtemplates_seq'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class GsRptFunnel(models.Model):
    id = models.IntegerField(primary_key=True)
    leadid = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pobox = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    assgn_first_name = models.CharField(max_length=30)
    assgn_last_name = models.CharField(max_length=30)
    smownerid = models.IntegerField()
    description = models.TextField()
    createdtime = models.DateTimeField()
    modifiedtime = models.DateTimeField()
    lead_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=80)
    company = models.CharField(max_length=100)
    leadstatus = models.CharField(max_length=50)
    leadsource = models.CharField(max_length=200)
    course = models.CharField(max_length=25)
    campaign_id = models.CharField(max_length=10)
    google_keyword = models.CharField(max_length=150)
    ref_domain = models.CharField(max_length=255)
    traffic_src = models.CharField(max_length=256)
    google_cookie = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'gs_rpt_funnel'

class ReportsReport(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    title = models.CharField(max_length=100)
    code = models.TextField()
    linenos = models.IntegerField()
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'reports_report'

class VtigerAccount(models.Model):
    accountid = models.ForeignKey('VtigerCrmentity', db_column='accountid', primary_key=True)
    account_no = models.CharField(max_length=100)
    accountname = models.CharField(max_length=100)
    parentid = models.IntegerField(blank=True, null=True)
    account_type = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=200, blank=True)
    annualrevenue = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True)
    ownership = models.CharField(max_length=50, blank=True)
    siccode = models.CharField(max_length=50, blank=True)
    tickersymbol = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    otherphone = models.CharField(max_length=30, blank=True)
    email1 = models.CharField(max_length=100, blank=True)
    email2 = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    fax = models.CharField(max_length=30, blank=True)
    employees = models.IntegerField(blank=True, null=True)
    emailoptout = models.CharField(max_length=3, blank=True)
    notify_owner = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_account'

class VtigerAccountbillads(models.Model):
    accountaddressid = models.ForeignKey(VtigerAccount, db_column='accountaddressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True)
    bill_code = models.CharField(max_length=30, blank=True)
    bill_country = models.CharField(max_length=30, blank=True)
    bill_state = models.CharField(max_length=30, blank=True)
    bill_street = models.CharField(max_length=250, blank=True)
    bill_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_accountbillads'

class VtigerAccountdepstatus(models.Model):
    deploymentstatusid = models.IntegerField(primary_key=True)
    deploymentstatus = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_accountdepstatus'

class VtigerAccountownership(models.Model):
    acctownershipid = models.IntegerField(primary_key=True)
    ownership = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_accountownership'

class VtigerAccountrating(models.Model):
    accountratingid = models.IntegerField(primary_key=True)
    rating = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_accountrating'

class VtigerAccountregion(models.Model):
    accountregionid = models.IntegerField(primary_key=True)
    region = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_accountregion'

class VtigerAccountscf(models.Model):
    accountid = models.ForeignKey(VtigerAccount, db_column='accountid', primary_key=True)
    cf_611 = models.CharField(max_length=255, blank=True)
    cf_612 = models.DateField(blank=True, null=True)
    cf_613 = models.CharField(max_length=50, blank=True)
    cf_614 = models.CharField(max_length=3, blank=True)
    cf_615 = models.CharField(max_length=3, blank=True)
    cf_617 = models.CharField(max_length=255, blank=True)
    cf_618 = models.CharField(max_length=255, blank=True)
    cf_619 = models.CharField(max_length=255, blank=True)
    cf_620 = models.TextField(blank=True)
    cf_621 = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    cf_622 = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    cf_623 = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    cf_624 = models.TextField(blank=True)
    cf_628 = models.CharField(max_length=50, blank=True)
    cf_635 = models.CharField(max_length=3, blank=True)
    cf_692 = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    cf_693 = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    cf_731 = models.CharField(max_length=255, blank=True)
    cf_732 = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_accountscf'

class VtigerAccountshipads(models.Model):
    accountaddressid = models.ForeignKey(VtigerAccount, db_column='accountaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True)
    ship_code = models.CharField(max_length=30, blank=True)
    ship_country = models.CharField(max_length=30, blank=True)
    ship_state = models.CharField(max_length=30, blank=True)
    ship_pobox = models.CharField(max_length=30, blank=True)
    ship_street = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_accountshipads'

class VtigerAccounttype(models.Model):
    accounttypeid = models.IntegerField(primary_key=True)
    accounttype = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_accounttype'

class VtigerAccounttypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_accounttype_seq'

class VtigerActionmapping(models.Model):
    actionid = models.IntegerField()
    actionname = models.CharField(max_length=200)
    securitycheck = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_actionmapping'

class VtigerActivity(models.Model):
    activityid = models.ForeignKey('VtigerCrmentity', db_column='activityid', primary_key=True)
    subject = models.CharField(max_length=100)
    semodule = models.CharField(max_length=20, blank=True)
    activitytype = models.CharField(max_length=200)
    date_start = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    time_start = models.CharField(max_length=50, blank=True)
    time_end = models.CharField(max_length=50, blank=True)
    sendnotification = models.CharField(max_length=3)
    duration_hours = models.CharField(max_length=200, blank=True)
    duration_minutes = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    eventstatus = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=150, blank=True)
    notime = models.CharField(max_length=3)
    visibility = models.CharField(max_length=50)
    recurringtype = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_activity'

class VtigerActivityReminder(models.Model):
    activity_id = models.IntegerField()
    reminder_time = models.IntegerField()
    reminder_sent = models.IntegerField()
    recurringid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activity_reminder'

class VtigerActivityReminderPopup(models.Model):
    reminderid = models.IntegerField(primary_key=True)
    semodule = models.CharField(max_length=100)
    recordid = models.IntegerField()
    date_start = models.DateField()
    time_start = models.CharField(max_length=100)
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activity_reminder_popup'

class VtigerActivityView(models.Model):
    activity_viewid = models.IntegerField(primary_key=True)
    activity_view = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activity_view'

class VtigerActivityViewSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activity_view_seq'

class VtigerActivitycf(models.Model):
    activityid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_activitycf'

class VtigerActivityproductrel(models.Model):
    activityid = models.IntegerField()
    productid = models.ForeignKey('VtigerProducts', db_column='productid')
    class Meta:
        managed = False
        db_table = 'vtiger_activityproductrel'

class VtigerActivitytype(models.Model):
    activitytypeid = models.IntegerField(primary_key=True)
    activitytype = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activitytype'

class VtigerActivitytypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activitytype_seq'

class VtigerActivsubtype(models.Model):
    activesubtypeid = models.IntegerField(primary_key=True)
    activsubtype = models.CharField(max_length=100, blank=True)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_activsubtype'

class VtigerAnnouncement(models.Model):
    creatorid = models.IntegerField()
    announcement = models.TextField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'vtiger_announcement'

class VtigerAssets(models.Model):
    assetsid = models.ForeignKey('VtigerCrmentity', db_column='assetsid', primary_key=True)
    asset_no = models.CharField(max_length=30)
    account = models.IntegerField()
    product = models.IntegerField()
    serialnumber = models.CharField(max_length=200)
    datesold = models.DateField()
    dateinservice = models.DateField()
    assetstatus = models.CharField(max_length=200, blank=True)
    tagnumber = models.CharField(max_length=300, blank=True)
    invoiceid = models.IntegerField(blank=True, null=True)
    shippingmethod = models.CharField(max_length=200, blank=True)
    shippingtrackingnumber = models.CharField(max_length=200, blank=True)
    assetname = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_assets'

class VtigerAssetscf(models.Model):
    assetsid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_assetscf'

class VtigerAssetstatus(models.Model):
    assetstatusid = models.IntegerField(primary_key=True)
    assetstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_assetstatus'

class VtigerAssetstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_assetstatus_seq'

class VtigerAsterisk(models.Model):
    server = models.CharField(max_length=30, blank=True)
    port = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    version = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_asterisk'

class VtigerAsteriskextensions(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    asterisk_extension = models.CharField(max_length=50, blank=True)
    use_asterisk = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_asteriskextensions'

class VtigerAsteriskincomingcalls(models.Model):
    from_number = models.CharField(max_length=50, blank=True)
    from_name = models.CharField(max_length=50, blank=True)
    to_number = models.CharField(max_length=50, blank=True)
    callertype = models.CharField(max_length=30, blank=True)
    flag = models.IntegerField(blank=True, null=True)
    timer = models.IntegerField(blank=True, null=True)
    refuid = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_asteriskincomingcalls'

class VtigerAsteriskincomingevents(models.Model):
    uid = models.CharField(primary_key=True, max_length=255)
    channel = models.CharField(max_length=100, blank=True)
    from_number = models.BigIntegerField(blank=True, null=True)
    from_name = models.CharField(max_length=100, blank=True)
    to_number = models.BigIntegerField(blank=True, null=True)
    callertype = models.CharField(max_length=100, blank=True)
    timer = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=3, blank=True)
    pbxrecordid = models.IntegerField(blank=True, null=True)
    relcrmid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_asteriskincomingevents'

class VtigerAttachments(models.Model):
    attachmentsid = models.ForeignKey('VtigerCrmentity', db_column='attachmentsid')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=100, blank=True)
    path = models.TextField(blank=True)
    subject = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_attachments'

class VtigerAttachmentsfolder(models.Model):
    folderid = models.IntegerField(primary_key=True)
    foldername = models.CharField(max_length=200)
    description = models.CharField(max_length=250, blank=True)
    createdby = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_attachmentsfolder'

class VtigerAttachmentsfolderSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_attachmentsfolder_seq'

class VtigerAuditTrial(models.Model):
    auditid = models.IntegerField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=255, blank=True)
    action = models.CharField(max_length=255, blank=True)
    recordid = models.CharField(max_length=20, blank=True)
    actiondate = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_audit_trial'

class VtigerAuditTrialSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_audit_trial_seq'

class VtigerBlocks(models.Model):
    blockid = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('VtigerTab', db_column='tabid')
    blocklabel = models.CharField(max_length=100)
    sequence = models.IntegerField(blank=True, null=True)
    show_title = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField()
    create_view = models.IntegerField()
    edit_view = models.IntegerField()
    detail_view = models.IntegerField()
    display_status = models.IntegerField()
    iscustom = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_blocks'

class VtigerBlocksSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_blocks_seq'

class VtigerBusinesstype(models.Model):
    businesstypeid = models.IntegerField(primary_key=True)
    businesstype = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_businesstype'

class VtigerCampaign(models.Model):
    campaign_no = models.CharField(max_length=100)
    campaignname = models.CharField(max_length=255, blank=True)
    campaigntype = models.CharField(max_length=200, blank=True)
    campaignstatus = models.CharField(max_length=200, blank=True)
    expectedrevenue = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    budgetcost = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    actualcost = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    expectedresponse = models.CharField(max_length=200, blank=True)
    numsent = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    sponsor = models.CharField(max_length=255, blank=True)
    targetaudience = models.CharField(max_length=255, blank=True)
    targetsize = models.IntegerField(blank=True, null=True)
    expectedresponsecount = models.IntegerField(blank=True, null=True)
    expectedsalescount = models.IntegerField(blank=True, null=True)
    expectedroi = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    actualresponsecount = models.IntegerField(blank=True, null=True)
    actualsalescount = models.IntegerField(blank=True, null=True)
    actualroi = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    campaignid = models.IntegerField()
    closingdate = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_campaign'

class VtigerCampaignStatus(models.Model):
    campaign_statusid = models.IntegerField(primary_key=True)
    campaign_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaign_status'

class VtigerCampaignStatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaign_status_seq'

class VtigerCampaignType(models.Model):
    campaign_typeid = models.IntegerField(primary_key=True)
    campaign_type = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaign_type'

class VtigerCampaignTypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaign_type_seq'

class VtigerCampaignaccountrel(models.Model):
    campaignid = models.IntegerField(blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    campaignrelstatusid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_campaignaccountrel'

class VtigerCampaigncontrel(models.Model):
    campaignid = models.IntegerField()
    contactid = models.ForeignKey('VtigerContactdetails', db_column='contactid')
    campaignrelstatusid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaigncontrel'

class VtigerCampaignleadrel(models.Model):
    campaignid = models.IntegerField()
    leadid = models.ForeignKey('VtigerLeaddetails', db_column='leadid')
    campaignrelstatusid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaignleadrel'

class VtigerCampaignrelstatus(models.Model):
    campaignrelstatusid = models.IntegerField(blank=True, null=True)
    campaignrelstatus = models.CharField(max_length=256, blank=True)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_campaignrelstatus'

class VtigerCampaignrelstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaignrelstatus_seq'

class VtigerCampaignscf(models.Model):
    campaignid = models.ForeignKey(VtigerCampaign, db_column='campaignid', primary_key=True)
    cf_610 = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_campaignscf'

class VtigerCampaignstatus(models.Model):
    campaignstatusid = models.IntegerField(primary_key=True)
    campaignstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaignstatus'

class VtigerCampaignstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaignstatus_seq'

class VtigerCampaigntype(models.Model):
    campaigntypeid = models.IntegerField(primary_key=True)
    campaigntype = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaigntype'

class VtigerCampaigntypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_campaigntype_seq'

class VtigerCarrier(models.Model):
    carrierid = models.IntegerField(primary_key=True)
    carrier = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_carrier'

class VtigerCarrierSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_carrier_seq'

class VtigerCf611(models.Model):
    cf_611id = models.IntegerField(primary_key=True)
    cf_611 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_611'

class VtigerCf611Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_611_seq'

class VtigerCf617(models.Model):
    cf_617id = models.IntegerField(primary_key=True)
    cf_617 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_617'

class VtigerCf617Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_617_seq'

class VtigerCf619(models.Model):
    cf_619id = models.IntegerField(primary_key=True)
    cf_619 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_619'

class VtigerCf619Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_619_seq'

class VtigerCf620(models.Model):
    cf_620id = models.IntegerField(primary_key=True)
    cf_620 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_620'

class VtigerCf620Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_620_seq'

class VtigerCf629Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_629_seq'

class VtigerCf699Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_699_seq'

class VtigerCf700Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_700_seq'

class VtigerCf701Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_701_seq'

class VtigerCf702Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_702_seq'

class VtigerCf707(models.Model):
    cf_707id = models.IntegerField(primary_key=True)
    cf_707 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_707'

class VtigerCf707Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_707_seq'

class VtigerCf708(models.Model):
    cf_708id = models.IntegerField(primary_key=True)
    cf_708 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_708'

class VtigerCf708Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_708_seq'

class VtigerCf709(models.Model):
    cf_709id = models.IntegerField(primary_key=True)
    cf_709 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_709'

class VtigerCf709Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_709_seq'

class VtigerCf710(models.Model):
    cf_710id = models.IntegerField(primary_key=True)
    cf_710 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_710'

class VtigerCf710Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_710_seq'

class VtigerCf714Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_714_seq'

class VtigerCf715Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_715_seq'

class VtigerCf716Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_716_seq'

class VtigerCf724(models.Model):
    cf_724id = models.IntegerField(primary_key=True)
    cf_724 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_724'

class VtigerCf724Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_724_seq'

class VtigerCf729(models.Model):
    cf_729id = models.IntegerField(primary_key=True)
    cf_729 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_729'

class VtigerCf729Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_729_seq'

class VtigerCf732(models.Model):
    cf_732id = models.IntegerField(primary_key=True)
    cf_732 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_732'

class VtigerCf732Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_732_seq'

class VtigerCf733(models.Model):
    cf_733id = models.IntegerField(primary_key=True)
    cf_733 = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_733'

class VtigerCf733Seq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cf_733_seq'

class VtigerChatMsg(models.Model):
    id = models.IntegerField(primary_key=True)
    chat_from = models.ForeignKey('VtigerChatUsers', db_column='chat_from')
    chat_to = models.IntegerField()
    born = models.DateTimeField(blank=True, null=True)
    msg = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'vtiger_chat_msg'

class VtigerChatPchat(models.Model):
    id = models.IntegerField(primary_key=True)
    msg = models.ForeignKey(VtigerChatMsg, db_column='msg', unique=True, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_chat_pchat'

class VtigerChatPvchat(models.Model):
    id = models.IntegerField(primary_key=True)
    msg = models.ForeignKey(VtigerChatMsg, db_column='msg', unique=True, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_chat_pvchat'

class VtigerChatUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    nick = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    ping = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_chat_users'

class VtigerCntactivityrel(models.Model):
    contactid = models.ForeignKey('VtigerContactdetails', db_column='contactid')
    activityid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_cntactivityrel'

class VtigerCompetitor(models.Model):
    competitorid = models.ForeignKey('VtigerCrmentity', db_column='competitorid', primary_key=True)
    competitorname = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True)
    strength = models.CharField(max_length=250, blank=True)
    weakness = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_competitor'

class VtigerContactaddress(models.Model):
    contactaddressid = models.ForeignKey('VtigerContactdetails', db_column='contactaddressid', primary_key=True)
    mailingcity = models.CharField(max_length=40, blank=True)
    mailingstreet = models.CharField(max_length=250, blank=True)
    mailingcountry = models.CharField(max_length=40, blank=True)
    othercountry = models.CharField(max_length=30, blank=True)
    mailingstate = models.CharField(max_length=30, blank=True)
    mailingpobox = models.CharField(max_length=30, blank=True)
    othercity = models.CharField(max_length=40, blank=True)
    otherstate = models.CharField(max_length=50, blank=True)
    mailingzip = models.CharField(max_length=30, blank=True)
    otherzip = models.CharField(max_length=30, blank=True)
    otherstreet = models.CharField(max_length=250, blank=True)
    otherpobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_contactaddress'

class VtigerContactdetails(models.Model):
    contactid = models.ForeignKey('VtigerCrmentity', db_column='contactid', primary_key=True)
    contact_no = models.CharField(max_length=100)
    accountid = models.IntegerField(blank=True, null=True)
    salutation = models.CharField(max_length=200, blank=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=80)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=30, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    reportsto = models.CharField(max_length=30, blank=True)
    training = models.CharField(max_length=50, blank=True)
    usertype = models.CharField(max_length=50, blank=True)
    contacttype = models.CharField(max_length=50, blank=True)
    otheremail = models.CharField(max_length=100, blank=True)
    secondaryemail = models.CharField(max_length=100, blank=True)
    donotcall = models.CharField(max_length=3, blank=True)
    emailoptout = models.CharField(max_length=3, blank=True)
    imagename = models.CharField(max_length=150, blank=True)
    reference = models.CharField(max_length=3, blank=True)
    notify_owner = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_contactdetails'

class VtigerContactscf(models.Model):
    contactid = models.ForeignKey(VtigerContactdetails, db_column='contactid', primary_key=True)
    cf_626 = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_contactscf'

class VtigerContactsubdetails(models.Model):
    contactsubscriptionid = models.ForeignKey(VtigerContactdetails, db_column='contactsubscriptionid', primary_key=True)
    homephone = models.CharField(max_length=50, blank=True)
    otherphone = models.CharField(max_length=50, blank=True)
    assistant = models.CharField(max_length=30, blank=True)
    assistantphone = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank=True, null=True)
    laststayintouchrequest = models.IntegerField(blank=True, null=True)
    laststayintouchsavedate = models.IntegerField(blank=True, null=True)
    leadsource = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_contactsubdetails'

class VtigerContacttype(models.Model):
    contacttypeid = models.IntegerField(primary_key=True)
    contacttype = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contacttype'

class VtigerContpotentialrel(models.Model):
    contactid = models.IntegerField()
    potentialid = models.ForeignKey('VtigerPotential', db_column='potentialid')
    class Meta:
        managed = False
        db_table = 'vtiger_contpotentialrel'

class VtigerContractPriority(models.Model):
    contract_priorityid = models.IntegerField(primary_key=True)
    contract_priority = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contract_priority'

class VtigerContractPrioritySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contract_priority_seq'

class VtigerContractStatus(models.Model):
    contract_statusid = models.IntegerField(primary_key=True)
    contract_status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contract_status'

class VtigerContractStatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contract_status_seq'

class VtigerContractType(models.Model):
    contract_typeid = models.IntegerField(primary_key=True)
    contract_type = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contract_type'

class VtigerContractTypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_contract_type_seq'

class VtigerConvertleadmapping(models.Model):
    cfmid = models.IntegerField(primary_key=True)
    leadfid = models.IntegerField()
    accountfid = models.IntegerField(blank=True, null=True)
    contactfid = models.IntegerField(blank=True, null=True)
    potentialfid = models.IntegerField(blank=True, null=True)
    editable = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_convertleadmapping'

class VtigerCrmentity(models.Model):
    crmid = models.IntegerField(primary_key=True)
    smcreatorid = models.IntegerField()
    smownerid = models.IntegerField()
    modifiedby = models.IntegerField()
    setype = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    createdtime = models.DateTimeField()
    modifiedtime = models.DateTimeField()
    viewedtime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True)
    version = models.IntegerField()
    presence = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_crmentity'

class VtigerCrmentitySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_crmentity_seq'

class VtigerCrmentitynotesrel(models.Model):
    crmid = models.IntegerField()
    notesid = models.ForeignKey('VtigerNotes', db_column='notesid')
    class Meta:
        managed = False
        db_table = 'vtiger_crmentitynotesrel'

class VtigerCrmentityrel(models.Model):
    crmid = models.IntegerField()
    module = models.CharField(max_length=100)
    relcrmid = models.IntegerField()
    relmodule = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'vtiger_crmentityrel'

class VtigerCronTask(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True)
    handler_file = models.CharField(unique=True, max_length=100, blank=True)
    frequency = models.IntegerField(blank=True, null=True)
    laststart = models.TextField(blank=True)
    lastend = models.TextField(blank=True)
    status = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=100, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_cron_task'

class VtigerCurrencies(models.Model):
    currencyid = models.IntegerField(primary_key=True)
    currency_name = models.CharField(max_length=200, blank=True)
    currency_code = models.CharField(max_length=50, blank=True)
    currency_symbol = models.CharField(max_length=11, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_currencies'

class VtigerCurrenciesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currencies_seq'

class VtigerCurrency(models.Model):
    currencyid = models.IntegerField(primary_key=True)
    currency = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency'

class VtigerCurrencyDecimalSeparator(models.Model):
    currency_decimal_separatorid = models.IntegerField(primary_key=True)
    currency_decimal_separator = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_decimal_separator'

class VtigerCurrencyDecimalSeparatorSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_decimal_separator_seq'

class VtigerCurrencyGroupingPattern(models.Model):
    currency_grouping_patternid = models.IntegerField(primary_key=True)
    currency_grouping_pattern = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_grouping_pattern'

class VtigerCurrencyGroupingPatternSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_grouping_pattern_seq'

class VtigerCurrencyGroupingSeparator(models.Model):
    currency_grouping_separatorid = models.IntegerField(primary_key=True)
    currency_grouping_separator = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_grouping_separator'

class VtigerCurrencyGroupingSeparatorSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_grouping_separator_seq'

class VtigerCurrencyInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    currency_name = models.CharField(max_length=100, blank=True)
    currency_code = models.CharField(max_length=100, blank=True)
    currency_symbol = models.CharField(max_length=30, blank=True)
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    currency_status = models.CharField(max_length=25, blank=True)
    defaultid = models.CharField(max_length=10)
    deleted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_info'

class VtigerCurrencyInfoSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_info_seq'

class VtigerCurrencySymbolPlacement(models.Model):
    currency_symbol_placementid = models.IntegerField(primary_key=True)
    currency_symbol_placement = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_symbol_placement'

class VtigerCurrencySymbolPlacementSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_currency_symbol_placement_seq'

class VtigerCustomaction(models.Model):
    cvid = models.ForeignKey('VtigerCustomview', db_column='cvid')
    subject = models.CharField(max_length=250)
    module = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_customaction'

class VtigerCustomerdetails(models.Model):
    customerid = models.ForeignKey(VtigerContactdetails, db_column='customerid', primary_key=True)
    portal = models.CharField(max_length=3, blank=True)
    support_start_date = models.DateField(blank=True, null=True)
    support_end_date = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_customerdetails'

class VtigerCustomerportalFields(models.Model):
    tabid = models.IntegerField()
    fieldid = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_customerportal_fields'

class VtigerCustomerportalPrefs(models.Model):
    tabid = models.IntegerField()
    prefkey = models.CharField(max_length=100)
    prefvalue = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_customerportal_prefs'

class VtigerCustomerportalTabs(models.Model):
    tabid = models.IntegerField(primary_key=True)
    visible = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_customerportal_tabs'

class VtigerCustomview(models.Model):
    cvid = models.IntegerField(primary_key=True)
    viewname = models.CharField(max_length=100)
    setdefault = models.IntegerField(blank=True, null=True)
    setmetrics = models.IntegerField(blank=True, null=True)
    entitytype = models.ForeignKey('VtigerTab', db_column='entitytype')
    status = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_customview'

class VtigerCustomviewSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_customview_seq'

class VtigerCvadvfilter(models.Model):
    cvid = models.ForeignKey(VtigerCustomview, db_column='cvid')
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True)
    comparator = models.CharField(max_length=10, blank=True)
    value = models.CharField(max_length=200, blank=True)
    groupid = models.IntegerField(blank=True, null=True)
    column_condition = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_cvadvfilter'

class VtigerCvadvfilterGrouping(models.Model):
    groupid = models.IntegerField()
    cvid = models.IntegerField()
    group_condition = models.CharField(max_length=255, blank=True)
    condition_expression = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_cvadvfilter_grouping'

class VtigerCvcolumnlist(models.Model):
    cvid = models.ForeignKey(VtigerCustomview, db_column='cvid')
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_cvcolumnlist'

class VtigerCvstdfilter(models.Model):
    cvid = models.ForeignKey(VtigerCustomview, db_column='cvid')
    columnname = models.CharField(max_length=250, blank=True)
    stdfilter = models.CharField(max_length=250, blank=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_cvstdfilter'

class VtigerDatashareGrp2Grp(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_groupid = models.IntegerField(blank=True, null=True)
    to_groupid = models.ForeignKey('VtigerGroups', db_column='to_groupid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_grp2grp'

class VtigerDatashareGrp2Role(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_groupid = models.IntegerField(blank=True, null=True)
    to_roleid = models.ForeignKey('VtigerRole', db_column='to_roleid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_grp2role'

class VtigerDatashareGrp2Rs(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_groupid = models.IntegerField(blank=True, null=True)
    to_roleandsubid = models.ForeignKey('VtigerRole', db_column='to_roleandsubid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_grp2rs'

class VtigerDatashareModuleRel(models.Model):
    shareid = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('VtigerTab', db_column='tabid')
    relationtype = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_module_rel'

class VtigerDatashareModuleRelSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_module_rel_seq'

class VtigerDatashareRelatedmodulePermission(models.Model):
    shareid = models.IntegerField()
    datashare_relatedmodule_id = models.IntegerField()
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_relatedmodule_permission'

class VtigerDatashareRelatedmodules(models.Model):
    datashare_relatedmodule_id = models.IntegerField(primary_key=True)
    tabid = models.ForeignKey('VtigerTab', db_column='tabid', blank=True, null=True)
    relatedto_tabid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_relatedmodules'

class VtigerDatashareRelatedmodulesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_relatedmodules_seq'

class VtigerDatashareRole2Group(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleid = models.ForeignKey('VtigerRole', db_column='share_roleid', blank=True, null=True)
    to_groupid = models.IntegerField(blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_role2group'

class VtigerDatashareRole2Role(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleid = models.CharField(max_length=255, blank=True)
    to_roleid = models.ForeignKey('VtigerRole', db_column='to_roleid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_role2role'

class VtigerDatashareRole2Rs(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleid = models.CharField(max_length=255, blank=True)
    to_roleandsubid = models.ForeignKey('VtigerRole', db_column='to_roleandsubid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_role2rs'

class VtigerDatashareRs2Grp(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleandsubid = models.ForeignKey('VtigerRole', db_column='share_roleandsubid', blank=True, null=True)
    to_groupid = models.IntegerField(blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_rs2grp'

class VtigerDatashareRs2Role(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleandsubid = models.CharField(max_length=255, blank=True)
    to_roleid = models.ForeignKey('VtigerRole', db_column='to_roleid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_rs2role'

class VtigerDatashareRs2Rs(models.Model):
    shareid = models.IntegerField(primary_key=True)
    share_roleandsubid = models.CharField(max_length=255, blank=True)
    to_roleandsubid = models.ForeignKey('VtigerRole', db_column='to_roleandsubid', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_datashare_rs2rs'

class VtigerDateFormat(models.Model):
    date_formatid = models.IntegerField(primary_key=True)
    date_format = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_date_format'

class VtigerDateFormatSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_date_format_seq'

class VtigerDealintimation(models.Model):
    dealintimationid = models.IntegerField(primary_key=True)
    dealname = models.CharField(unique=True, max_length=100)
    intimationamount = models.IntegerField()
    dealprobability = models.DecimalField(max_digits=3, decimal_places=2)
    dealintimationactive = models.IntegerField(blank=True, null=True)
    fromname = models.CharField(max_length=120)
    fromemailid = models.CharField(max_length=100)
    notifyemails = models.CharField(max_length=50)
    notifybccemails = models.CharField(max_length=50)
    notifyccmails = models.CharField(max_length=50)
    notifypotentialowner = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_dealintimation'

class VtigerDefOrgField(models.Model):
    tabid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(primary_key=True)
    visible = models.IntegerField(blank=True, null=True)
    readonly = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_def_org_field'

class VtigerDefOrgShare(models.Model):
    ruleid = models.IntegerField(primary_key=True)
    tabid = models.IntegerField()
    permission = models.ForeignKey('VtigerOrgShareActionMapping', db_column='permission', blank=True, null=True)
    editstatus = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_def_org_share'

class VtigerDefOrgShareSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_def_org_share_seq'

class VtigerDefaultcv(models.Model):
    tabid = models.ForeignKey('VtigerTab', db_column='tabid', primary_key=True)
    defaultviewname = models.CharField(max_length=50)
    query = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_defaultcv'

class VtigerDownloadpurpose(models.Model):
    downloadpurposeid = models.IntegerField(primary_key=True)
    purpose = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_downloadpurpose'

class VtigerDurationMinutes(models.Model):
    minutesid = models.IntegerField(primary_key=True)
    duration_minutes = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_duration_minutes'

class VtigerDurationMinutesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_duration_minutes_seq'

class VtigerDurationhrs(models.Model):
    hrsid = models.IntegerField(primary_key=True)
    hrs = models.CharField(max_length=50, blank=True)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_durationhrs'

class VtigerDurationmins(models.Model):
    minsid = models.IntegerField(primary_key=True)
    mins = models.CharField(max_length=50, blank=True)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_durationmins'

class VtigerEmailAccess(models.Model):
    crmid = models.IntegerField(blank=True, null=True)
    mailid = models.IntegerField(blank=True, null=True)
    accessdate = models.DateField(blank=True, null=True)
    accesstime = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_email_access'

class VtigerEmailTrack(models.Model):
    crmid = models.IntegerField(blank=True, null=True)
    mailid = models.IntegerField(blank=True, null=True)
    access_count = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_email_track'

class VtigerEmaildetails(models.Model):
    emailid = models.IntegerField(primary_key=True)
    from_email = models.CharField(max_length=50)
    to_email = models.TextField(blank=True)
    cc_email = models.TextField(blank=True)
    bcc_email = models.TextField(blank=True)
    assigned_user_email = models.CharField(max_length=50)
    idlists = models.TextField(blank=True)
    email_flag = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'vtiger_emaildetails'

class VtigerEmailtemplates(models.Model):
    foldername = models.CharField(max_length=100, blank=True)
    templatename = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    deleted = models.IntegerField()
    templateid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_emailtemplates'

class VtigerEmailtemplatesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_emailtemplates_seq'

class VtigerEntityname(models.Model):
    tabid = models.ForeignKey('VtigerTab', db_column='tabid')
    modulename = models.CharField(max_length=50)
    tablename = models.CharField(max_length=100)
    fieldname = models.CharField(max_length=150)
    entityidfield = models.CharField(max_length=150)
    entityidcolumn = models.CharField(max_length=150)
    class Meta:
        managed = False
        db_table = 'vtiger_entityname'

class VtigerEvaluationstatus(models.Model):
    evalstatusid = models.IntegerField(primary_key=True)
    status = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_evaluationstatus'

class VtigerEventhandlerModule(models.Model):
    eventhandler_module_id = models.IntegerField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True)
    handler_class = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_eventhandler_module'

class VtigerEventhandlerModuleSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_eventhandler_module_seq'

class VtigerEventhandlers(models.Model):
    eventhandler_id = models.IntegerField(unique=True)
    event_name = models.CharField(max_length=100)
    handler_path = models.CharField(max_length=400)
    handler_class = models.CharField(max_length=100)
    cond = models.TextField(blank=True)
    is_active = models.IntegerField()
    dependent_on = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'vtiger_eventhandlers'

class VtigerEventhandlersSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_eventhandlers_seq'

class VtigerEventstatus(models.Model):
    eventstatusid = models.IntegerField(primary_key=True)
    eventstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_eventstatus'

class VtigerEventstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_eventstatus_seq'

class VtigerExpectedresponse(models.Model):
    expectedresponseid = models.IntegerField(primary_key=True)
    expectedresponse = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_expectedresponse'

class VtigerExpectedresponseSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_expectedresponse_seq'

class VtigerFaq(models.Model):
    id = models.ForeignKey(VtigerCrmentity, db_column='id')
    faq_no = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100, blank=True)
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    category = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_faq'

class VtigerFaqcategories(models.Model):
    faqcategories_id = models.IntegerField(primary_key=True)
    faqcategories = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_faqcategories'

class VtigerFaqcategoriesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_faqcategories_seq'

class VtigerFaqcomments(models.Model):
    commentid = models.IntegerField(primary_key=True)
    faqid = models.ForeignKey(VtigerFaq, db_column='faqid', blank=True, null=True)
    comments = models.TextField(blank=True)
    createdtime = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'vtiger_faqcomments'

class VtigerFaqstatus(models.Model):
    faqstatus_id = models.IntegerField(primary_key=True)
    faqstatus = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_faqstatus'

class VtigerFaqstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_faqstatus_seq'

class VtigerField(models.Model):
    tabid = models.ForeignKey('VtigerTab', db_column='tabid')
    fieldid = models.IntegerField(primary_key=True)
    columnname = models.CharField(max_length=30)
    tablename = models.CharField(max_length=50)
    generatedtype = models.IntegerField()
    uitype = models.CharField(max_length=30)
    fieldname = models.CharField(max_length=50)
    fieldlabel = models.CharField(max_length=50)
    readonly = models.IntegerField()
    presence = models.IntegerField()
    defaultvalue = models.TextField(blank=True)
    maximumlength = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    block = models.IntegerField(blank=True, null=True)
    displaytype = models.IntegerField(blank=True, null=True)
    typeofdata = models.CharField(max_length=100, blank=True)
    quickcreate = models.IntegerField()
    quickcreatesequence = models.IntegerField(blank=True, null=True)
    info_type = models.CharField(max_length=20, blank=True)
    masseditable = models.IntegerField()
    helpinfo = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_field'

class VtigerFieldSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_field_seq'

class VtigerFieldformulas(models.Model):
    expressionid = models.IntegerField(primary_key=True)
    modulename = models.CharField(max_length=100, blank=True)
    expression_engine = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_fieldformulas'

class VtigerFieldformulasSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_fieldformulas_seq'

class VtigerFieldmodulerel(models.Model):
    fieldid = models.IntegerField()
    module = models.CharField(max_length=100)
    relmodule = models.CharField(max_length=100)
    status = models.CharField(max_length=10, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_fieldmodulerel'

class VtigerFiles(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=36, blank=True)
    content = models.TextField(blank=True)
    deleted = models.IntegerField()
    date_entered = models.DateTimeField()
    assigned_user_id = models.CharField(max_length=36, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_files'

class VtigerFreetaggedObjects(models.Model):
    tag_id = models.IntegerField()
    tagger_id = models.IntegerField()
    object_id = models.IntegerField()
    tagged_on = models.DateTimeField()
    module = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'vtiger_freetagged_objects'

class VtigerFreetags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=50)
    raw_tag = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'vtiger_freetags'

class VtigerFreetagsSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_freetags_seq'

class VtigerGlacct(models.Model):
    glacctid = models.IntegerField(primary_key=True)
    glacct = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_glacct'

class VtigerGlacctSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_glacct_seq'

class VtigerGroup2Grouprel(models.Model):
    groupid = models.ForeignKey('VtigerGroups', db_column='groupid')
    containsgroupid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_group2grouprel'

class VtigerGroup2Role(models.Model):
    groupid = models.IntegerField()
    roleid = models.ForeignKey('VtigerRole', db_column='roleid')
    class Meta:
        managed = False
        db_table = 'vtiger_group2role'

class VtigerGroup2Rs(models.Model):
    groupid = models.IntegerField()
    roleandsubid = models.ForeignKey('VtigerRole', db_column='roleandsubid')
    class Meta:
        managed = False
        db_table = 'vtiger_group2rs'

class VtigerGroups(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(unique=True, max_length=100, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_groups'

class VtigerHeaders(models.Model):
    fileid = models.IntegerField(primary_key=True)
    headernames = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'vtiger_headers'

class VtigerHomeLayout(models.Model):
    userid = models.IntegerField(primary_key=True)
    layout = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_home_layout'

class VtigerHomedashbd(models.Model):
    stuffid = models.ForeignKey('VtigerHomestuff', db_column='stuffid')
    dashbdname = models.CharField(max_length=100, blank=True)
    dashbdtype = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_homedashbd'

class VtigerHomedefault(models.Model):
    stuffid = models.ForeignKey('VtigerHomestuff', db_column='stuffid')
    hometype = models.CharField(max_length=30)
    maxentries = models.IntegerField(blank=True, null=True)
    setype = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_homedefault'

class VtigerHomemodule(models.Model):
    stuffid = models.ForeignKey('VtigerHomestuff', db_column='stuffid')
    modulename = models.CharField(max_length=100, blank=True)
    maxentries = models.IntegerField()
    customviewid = models.IntegerField()
    setype = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'vtiger_homemodule'

class VtigerHomemoduleflds(models.Model):
    stuffid = models.ForeignKey(VtigerHomemodule, db_column='stuffid', blank=True, null=True)
    fieldname = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_homemoduleflds'

class VtigerHomereportchart(models.Model):
    stuffid = models.IntegerField(primary_key=True)
    reportid = models.IntegerField(blank=True, null=True)
    reportcharttype = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_homereportchart'

class VtigerHomerss(models.Model):
    stuffid = models.ForeignKey('VtigerHomestuff', db_column='stuffid')
    url = models.CharField(max_length=100, blank=True)
    maxentries = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_homerss'

class VtigerHomestuff(models.Model):
    stuffid = models.IntegerField()
    stuffsequence = models.IntegerField()
    stufftype = models.CharField(max_length=100, blank=True)
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    visible = models.IntegerField()
    stufftitle = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_homestuff'

class VtigerHomestuffSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_homestuff_seq'

class VtigerImport3916(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    recordid = models.IntegerField(blank=True, null=True)
    firstname = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    lastname = models.TextField(blank=True)
    assigned_user_id = models.TextField(blank=True)
    email = models.TextField(blank=True)
    city = models.TextField(blank=True)
    cf_607 = models.TextField(blank=True)
    cf_625 = models.TextField(blank=True)
    cf_630 = models.TextField(blank=True)
    cf_707 = models.TextField(blank=True)
    cf_609 = models.TextField(blank=True)
    cf_708 = models.TextField(blank=True)
    cf_696 = models.TextField(blank=True)
    cf_709 = models.TextField(blank=True)
    cf_678 = models.TextField(blank=True)
    cf_677 = models.TextField(blank=True)
    country = models.TextField(blank=True)
    state = models.TextField(blank=True)
    description = models.TextField(blank=True)
    cf_637 = models.TextField(blank=True)
    cf_638 = models.TextField(blank=True)
    company = models.TextField(blank=True)
    leadstatus = models.TextField(blank=True)
    cf_724 = models.TextField(blank=True)
    cf_636 = models.TextField(blank=True)
    cf_710 = models.TextField(blank=True)
    cf_633 = models.TextField(blank=True)
    createdtime = models.TextField(blank=True)
    cf_634 = models.TextField(blank=True)
    cf_632 = models.TextField(blank=True)
    cf_729 = models.TextField(blank=True)
    cf_639 = models.TextField(blank=True)
    leadsource = models.TextField(blank=True)
    cf_689 = models.TextField(blank=True)
    cf_679 = models.TextField(blank=True)
    cf_640 = models.TextField(blank=True)
    cf_691 = models.TextField(blank=True)
    cf_690 = models.TextField(blank=True)
    cf_694 = models.TextField(blank=True)
    cf_706 = models.TextField(blank=True)
    cf_704 = models.TextField(blank=True)
    cf_711 = models.TextField(blank=True)
    cf_712 = models.TextField(blank=True)
    cf_727 = models.TextField(blank=True)
    cf_721 = models.TextField(blank=True)
    cf_722 = models.TextField(blank=True)
    cf_723 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_import_3916'

class VtigerImport3950(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    recordid = models.IntegerField(blank=True, null=True)
    cf_729 = models.TextField(blank=True)
    leadsource = models.TextField(blank=True)
    cf_679 = models.TextField(blank=True)
    lastname = models.TextField(blank=True)
    firstname = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    cf_607 = models.TextField(blank=True)
    city = models.TextField(blank=True)
    country = models.TextField(blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_import_3950'

class VtigerImport3969(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    recordid = models.IntegerField(blank=True, null=True)
    cf_607 = models.TextField(blank=True)
    firstname = models.TextField(blank=True)
    lastname = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    city = models.TextField(blank=True)
    leadsource = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_import_3969'

class VtigerImportLocks(models.Model):
    vtiger_import_lock_id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    tabid = models.IntegerField()
    importid = models.IntegerField()
    locked_since = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_import_locks'

class VtigerImportLocksSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_import_locks_seq'

class VtigerImportMaps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=36)
    module = models.CharField(max_length=36)
    content = models.TextField(blank=True)
    has_header = models.IntegerField()
    deleted = models.IntegerField()
    date_entered = models.DateTimeField()
    date_modified = models.DateTimeField()
    assigned_user_id = models.CharField(max_length=36, blank=True)
    is_published = models.CharField(max_length=3)
    class Meta:
        managed = False
        db_table = 'vtiger_import_maps'

class VtigerImportQueue(models.Model):
    importid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    tabid = models.IntegerField()
    field_mapping = models.TextField(blank=True)
    default_values = models.TextField(blank=True)
    merge_type = models.IntegerField(blank=True, null=True)
    merge_fields = models.TextField(blank=True)
    status = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_import_queue'

class VtigerImportQueueSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_import_queue_seq'

class VtigerIndustry(models.Model):
    industryid = models.IntegerField(primary_key=True)
    industry = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_industry'

class VtigerIndustrySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_industry_seq'

class VtigerIntermediate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lead_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    process_status = models.CharField(max_length=255, blank=True)
    insert_timestamp = models.DateTimeField()
    leadsource = models.TextField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    traffic_source = models.TextField(blank=True)
    cookie = models.TextField(blank=True)
    keyword = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_intermediate'

class VtigerInventoryTandc(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    tandc = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_inventory_tandc'

class VtigerInventoryTandcSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_inventory_tandc_seq'

class VtigerInventorynotification(models.Model):
    notificationid = models.IntegerField(primary_key=True)
    notificationname = models.CharField(max_length=200, blank=True)
    notificationsubject = models.CharField(max_length=200, blank=True)
    notificationbody = models.TextField(blank=True)
    label = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_inventorynotification'

class VtigerInventorynotificationSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_inventorynotification_seq'

class VtigerInventoryproductrel(models.Model):
    id = models.IntegerField(blank=True, null=True)
    productid = models.IntegerField(blank=True, null=True)
    sequence_no = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    listprice = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    incrementondel = models.IntegerField()
    lineitem_id = models.IntegerField(primary_key=True)
    tax1 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    tax2 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    tax3 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_inventoryproductrel'

class VtigerInventoryshippingrel(models.Model):
    id = models.IntegerField(blank=True, null=True)
    shtax1 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    shtax2 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    shtax3 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_inventoryshippingrel'

class VtigerInventorysubproductrel(models.Model):
    id = models.IntegerField()
    sequence_no = models.IntegerField()
    productid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_inventorysubproductrel'

class VtigerInventorytaxinfo(models.Model):
    taxid = models.IntegerField(primary_key=True)
    taxname = models.CharField(max_length=50, blank=True)
    taxlabel = models.CharField(max_length=50, blank=True)
    percentage = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_inventorytaxinfo'

class VtigerInventorytaxinfoSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_inventorytaxinfo_seq'

class VtigerInvitees(models.Model):
    activityid = models.IntegerField()
    inviteeid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_invitees'

class VtigerInvoice(models.Model):
    invoiceid = models.IntegerField()
    subject = models.CharField(max_length=100, blank=True)
    salesorderid = models.ForeignKey('VtigerSalesorder', db_column='salesorderid', blank=True, null=True)
    customerno = models.CharField(max_length=100, blank=True)
    contactid = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True)
    invoicedate = models.DateField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    invoiceterms = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    salescommission = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    exciseduty = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    shipping = models.CharField(max_length=100, blank=True)
    accountid = models.IntegerField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True)
    purchaseorder = models.CharField(max_length=200, blank=True)
    invoicestatus = models.CharField(max_length=200, blank=True)
    invoice_no = models.CharField(max_length=100, blank=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    class Meta:
        managed = False
        db_table = 'vtiger_invoice'

class VtigerInvoiceRecurringInfo(models.Model):
    salesorderid = models.IntegerField(blank=True, null=True)
    recurring_frequency = models.CharField(max_length=200, blank=True)
    start_period = models.DateField(blank=True, null=True)
    end_period = models.DateField(blank=True, null=True)
    last_recurring_date = models.DateField(blank=True, null=True)
    payment_duration = models.CharField(max_length=200, blank=True)
    invoice_status = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_invoice_recurring_info'

class VtigerInvoicebillads(models.Model):
    invoicebilladdressid = models.ForeignKey(VtigerInvoice, db_column='invoicebilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True)
    bill_code = models.CharField(max_length=30, blank=True)
    bill_country = models.CharField(max_length=30, blank=True)
    bill_state = models.CharField(max_length=30, blank=True)
    bill_street = models.CharField(max_length=250, blank=True)
    bill_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_invoicebillads'

class VtigerInvoicecf(models.Model):
    invoiceid = models.ForeignKey(VtigerInvoice, db_column='invoiceid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_invoicecf'

class VtigerInvoiceshipads(models.Model):
    invoiceshipaddressid = models.ForeignKey(VtigerInvoice, db_column='invoiceshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True)
    ship_code = models.CharField(max_length=30, blank=True)
    ship_country = models.CharField(max_length=30, blank=True)
    ship_state = models.CharField(max_length=30, blank=True)
    ship_street = models.CharField(max_length=250, blank=True)
    ship_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_invoiceshipads'

class VtigerInvoicestatus(models.Model):
    invoicestatusid = models.IntegerField(primary_key=True)
    invoicestatus = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_invoicestatus'

class VtigerInvoicestatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_invoicestatus_seq'

class VtigerInvoicestatushistory(models.Model):
    historyid = models.IntegerField(primary_key=True)
    invoiceid = models.ForeignKey(VtigerInvoice, db_column='invoiceid')
    accountname = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    invoicestatus = models.CharField(max_length=200, blank=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_invoicestatushistory'

class VtigerLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    prefix = models.CharField(max_length=10, blank=True)
    label = models.CharField(max_length=30, blank=True)
    lastupdated = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    isdefault = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_language'

class VtigerLanguageSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_language_seq'

class VtigerLar(models.Model):
    larid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    createdby = models.ForeignKey('VtigerUsers', db_column='createdby')
    createdon = models.DateField()
    class Meta:
        managed = False
        db_table = 'vtiger_lar'

class VtigerLeadView(models.Model):
    lead_viewid = models.IntegerField(primary_key=True)
    lead_view = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_lead_view'

class VtigerLeadViewSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_lead_view_seq'

class VtigerLeadacctrel(models.Model):
    leadid = models.ForeignKey('VtigerLeaddetails', db_column='leadid', primary_key=True)
    accountid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadacctrel'

class VtigerLeadaddress(models.Model):
    leadaddressid = models.ForeignKey('VtigerLeaddetails', db_column='leadaddressid', primary_key=True)
    city = models.CharField(max_length=30, blank=True)
    code = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    pobox = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    lane = models.CharField(max_length=250, blank=True)
    leadaddresstype = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_leadaddress'

class VtigerLeadcontrel(models.Model):
    leadid = models.ForeignKey('VtigerLeaddetails', db_column='leadid', primary_key=True)
    contactid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadcontrel'

class VtigerLeaddetails(models.Model):
    leadid = models.ForeignKey(VtigerCrmentity, db_column='leadid', primary_key=True)
    lead_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    interest = models.CharField(max_length=50, blank=True)
    firstname = models.CharField(max_length=40, blank=True)
    salutation = models.CharField(max_length=200, blank=True)
    lastname = models.CharField(max_length=80)
    company = models.CharField(max_length=100)
    annualrevenue = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True)
    campaign = models.CharField(max_length=30, blank=True)
    rating = models.CharField(max_length=200, blank=True)
    leadstatus = models.CharField(max_length=50, blank=True)
    leadsource = models.CharField(max_length=200, blank=True)
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
        managed = False
        db_table = 'vtiger_leaddetails'

class VtigerLeadpotrel(models.Model):
    leadid = models.IntegerField(unique=True)
    potentialid = models.ForeignKey('VtigerPotential', db_column='potentialid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_leadpotrel'

class VtigerLeadscf(models.Model):
    leadid = models.ForeignKey(VtigerLeaddetails, db_column='leadid', primary_key=True)
    cf_607 = models.CharField(max_length=25, blank=True)
    cf_609 = models.CharField(max_length=10, blank=True)
    cf_625 = models.DateField(blank=True, null=True)
    cf_630 = models.CharField(max_length=25, blank=True)
    cf_632 = models.CharField(max_length=150, blank=True)
    cf_633 = models.CharField(max_length=255, blank=True)
    cf_634 = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    cf_636 = models.DateField(blank=True, null=True)
    cf_637 = models.CharField(max_length=255, blank=True)
    cf_638 = models.TextField(blank=True)
    cf_639 = models.TextField(blank=True)
    cf_640 = models.TextField(blank=True)
    cf_677 = models.TextField(blank=True)
    cf_678 = models.CharField(max_length=25, blank=True)
    cf_679 = models.CharField(max_length=256, blank=True)
    cf_689 = models.CharField(max_length=255, blank=True)
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
    cf_733 = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_leadscf'

class VtigerLeadsource(models.Model):
    leadsourceid = models.IntegerField(primary_key=True)
    leadsource = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadsource'

class VtigerLeadsourceSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadsource_seq'

class VtigerLeadstage(models.Model):
    leadstageid = models.IntegerField(primary_key=True)
    stage = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadstage'

class VtigerLeadstatus(models.Model):
    leadstatusid = models.IntegerField(primary_key=True)
    leadstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadstatus'

class VtigerLeadstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_leadstatus_seq'

class VtigerLeadsubdetails(models.Model):
    leadsubscriptionid = models.ForeignKey(VtigerLeaddetails, db_column='leadsubscriptionid', primary_key=True)
    website = models.CharField(max_length=255, blank=True)
    callornot = models.IntegerField(blank=True, null=True)
    readornot = models.IntegerField(blank=True, null=True)
    empct = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_leadsubdetails'

class VtigerLicencekeystatus(models.Model):
    licencekeystatusid = models.IntegerField(primary_key=True)
    licencekeystatus = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_licencekeystatus'

class VtigerLinks(models.Model):
    linkid = models.IntegerField(primary_key=True)
    tabid = models.IntegerField(blank=True, null=True)
    linktype = models.CharField(max_length=20, blank=True)
    linklabel = models.CharField(max_length=30, blank=True)
    linkurl = models.CharField(max_length=255, blank=True)
    linkicon = models.CharField(max_length=100, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    handler_path = models.CharField(max_length=128, blank=True)
    handler_class = models.CharField(max_length=32, blank=True)
    handler = models.CharField(max_length=32, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_links'

class VtigerLinksSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_links_seq'

class VtigerLoginhistory(models.Model):
    login_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=25)
    user_ip = models.CharField(max_length=25)
    logout_time = models.DateTimeField()
    login_time = models.DateTimeField()
    status = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_loginhistory'

class VtigerMailAccounts(models.Model):
    account_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    display_name = models.CharField(max_length=50, blank=True)
    mail_id = models.CharField(max_length=50, blank=True)
    account_name = models.CharField(max_length=50, blank=True)
    mail_protocol = models.CharField(max_length=20, blank=True)
    mail_username = models.CharField(max_length=50)
    mail_password = models.CharField(max_length=250)
    mail_servername = models.CharField(max_length=50, blank=True)
    box_refresh = models.IntegerField(blank=True, null=True)
    mails_per_page = models.IntegerField(blank=True, null=True)
    ssltype = models.CharField(max_length=50, blank=True)
    sslmeth = models.CharField(max_length=50, blank=True)
    int_mailer = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True)
    set_default = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mail_accounts'

class VtigerMailchimp(models.Model):
    mailchimpid = models.IntegerField(blank=True, null=True)
    mailchimpname = models.CharField(max_length=255, blank=True)
    campaign_no = models.CharField(max_length=100, blank=True)
    campaign_type = models.CharField(max_length=200, blank=True)
    campaign_status = models.CharField(max_length=200, blank=True)
    lastsynchronization = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailchimp'

class VtigerMailchimpSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    apikey = models.CharField(max_length=100)
    listid = models.CharField(max_length=50)
    newsubscribertype = models.CharField(max_length=50)
    lastsyncdate = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'vtiger_mailchimp_settings'

class VtigerMailchimpcf(models.Model):
    mailchimpid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailchimpcf'

class VtigerMailchimpsyncdiff(models.Model):
    crmid = models.IntegerField()
    module = models.CharField(max_length=100)
    relcrmid = models.IntegerField()
    relmodule = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'vtiger_mailchimpsyncdiff'

class VtigerMailmanagerMailattachments(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    muid = models.IntegerField(blank=True, null=True)
    aname = models.CharField(max_length=100, blank=True)
    lastsavedtime = models.IntegerField(blank=True, null=True)
    attachid = models.IntegerField()
    path = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_mailmanager_mailattachments'

class VtigerMailmanagerMailrecord(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    mfrom = models.CharField(max_length=255, blank=True)
    mto = models.CharField(max_length=255, blank=True)
    mcc = models.CharField(max_length=500, blank=True)
    mbcc = models.CharField(max_length=500, blank=True)
    mdate = models.CharField(max_length=20, blank=True)
    msubject = models.CharField(max_length=500, blank=True)
    mbody = models.TextField(blank=True)
    mcharset = models.CharField(max_length=10, blank=True)
    misbodyhtml = models.IntegerField(blank=True, null=True)
    mplainmessage = models.IntegerField(blank=True, null=True)
    mhtmlmessage = models.IntegerField(blank=True, null=True)
    muniqueid = models.CharField(max_length=500, blank=True)
    mbodyparsed = models.IntegerField(blank=True, null=True)
    muid = models.IntegerField(blank=True, null=True)
    lastsavedtime = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailmanager_mailrecord'

class VtigerMailmanagerMailrel(models.Model):
    mailuid = models.CharField(max_length=999, blank=True)
    crmid = models.IntegerField(blank=True, null=True)
    emailid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailmanager_mailrel'

class VtigerMailscanner(models.Model):
    scannerid = models.IntegerField(primary_key=True)
    scannername = models.CharField(max_length=30, blank=True)
    server = models.CharField(max_length=100, blank=True)
    protocol = models.CharField(max_length=10, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    ssltype = models.CharField(max_length=10, blank=True)
    sslmethod = models.CharField(max_length=30, blank=True)
    connecturl = models.CharField(max_length=255, blank=True)
    searchfor = models.CharField(max_length=10, blank=True)
    markas = models.CharField(max_length=10, blank=True)
    isvalid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailscanner'

class VtigerMailscannerActions(models.Model):
    actionid = models.IntegerField(primary_key=True)
    scannerid = models.IntegerField(blank=True, null=True)
    actiontype = models.CharField(max_length=10, blank=True)
    module = models.CharField(max_length=30, blank=True)
    lookup = models.CharField(max_length=30, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailscanner_actions'

class VtigerMailscannerFolders(models.Model):
    folderid = models.IntegerField(primary_key=True)
    scannerid = models.IntegerField(blank=True, null=True)
    foldername = models.CharField(max_length=255, blank=True)
    lastscan = models.CharField(max_length=30, blank=True)
    rescan = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailscanner_folders'

class VtigerMailscannerIds(models.Model):
    scannerid = models.IntegerField(blank=True, null=True)
    messageid = models.TextField(blank=True)
    crmid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailscanner_ids'

class VtigerMailscannerRuleactions(models.Model):
    ruleid = models.IntegerField(blank=True, null=True)
    actionid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailscanner_ruleactions'

class VtigerMailscannerRules(models.Model):
    ruleid = models.IntegerField(primary_key=True)
    scannerid = models.IntegerField(blank=True, null=True)
    fromaddress = models.CharField(max_length=255, blank=True)
    toaddress = models.CharField(max_length=255, blank=True)
    subjectop = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    bodyop = models.CharField(max_length=20, blank=True)
    body = models.CharField(max_length=255, blank=True)
    matchusing = models.CharField(max_length=5, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_mailscanner_rules'

class VtigerManufacturer(models.Model):
    manufacturerid = models.IntegerField(primary_key=True)
    manufacturer = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_manufacturer'

class VtigerManufacturerSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_manufacturer_seq'

class VtigerMobileAlerts(models.Model):
    id = models.IntegerField(primary_key=True)
    handler_path = models.CharField(max_length=500, blank=True)
    handler_class = models.CharField(max_length=50, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_mobile_alerts'

class VtigerModcomments(models.Model):
    modcommentsid = models.IntegerField(blank=True, null=True)
    commentcontent = models.TextField(blank=True)
    related_to = models.CharField(max_length=100)
    parent_comments = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_modcomments'

class VtigerModcommentscf(models.Model):
    modcommentsid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_modcommentscf'

class VtigerModentityNum(models.Model):
    num_id = models.IntegerField(unique=True)
    semodule = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    start_id = models.CharField(max_length=50)
    cur_id = models.CharField(max_length=50)
    active = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'vtiger_modentity_num'

class VtigerModentityNumSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_modentity_num_seq'

class VtigerModtrackerBasic(models.Model):
    id = models.IntegerField(primary_key=True)
    crmid = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True)
    whodid = models.IntegerField(blank=True, null=True)
    changedon = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_modtracker_basic'

class VtigerModtrackerBasicSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_modtracker_basic_seq'

class VtigerModtrackerDetail(models.Model):
    id = models.IntegerField(blank=True, null=True)
    fieldname = models.CharField(max_length=100, blank=True)
    prevalue = models.TextField(blank=True)
    postvalue = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_modtracker_detail'

class VtigerModtrackerTabs(models.Model):
    tabid = models.IntegerField(primary_key=True)
    visible = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_modtracker_tabs'

class VtigerModuleowners(models.Model):
    tabid = models.ForeignKey('VtigerTab', db_column='tabid', primary_key=True)
    user_id = models.CharField(max_length=11)
    class Meta:
        managed = False
        db_table = 'vtiger_moduleowners'

class VtigerNotebookContents(models.Model):
    userid = models.IntegerField()
    notebookid = models.IntegerField()
    contents = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_notebook_contents'

class VtigerNotes(models.Model):
    notesid = models.ForeignKey(VtigerCrmentity, db_column='notesid')
    note_no = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    filename = models.CharField(max_length=200, blank=True)
    notecontent = models.TextField(blank=True)
    folderid = models.IntegerField()
    filetype = models.CharField(max_length=50, blank=True)
    filelocationtype = models.CharField(max_length=5, blank=True)
    filedownloadcount = models.IntegerField(blank=True, null=True)
    filestatus = models.IntegerField(blank=True, null=True)
    filesize = models.IntegerField()
    fileversion = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_notes'

class VtigerNotescf(models.Model):
    notesid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_notescf'

class VtigerNotificationscheduler(models.Model):
    schedulednotificationid = models.IntegerField(primary_key=True)
    schedulednotificationname = models.CharField(unique=True, max_length=200, blank=True)
    active = models.IntegerField(blank=True, null=True)
    notificationsubject = models.CharField(max_length=200, blank=True)
    notificationbody = models.TextField(blank=True)
    label = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_notificationscheduler'

class VtigerNotificationschedulerSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_notificationscheduler_seq'

class VtigerOpportunityType(models.Model):
    opptypeid = models.IntegerField(primary_key=True)
    opportunity_type = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_opportunity_type'

class VtigerOpportunityTypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_opportunity_type_seq'

class VtigerOpportunitystage(models.Model):
    potstageid = models.IntegerField(primary_key=True)
    stage = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    probability = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_opportunitystage'

class VtigerOrgShareAction2Tab(models.Model):
    share_action_id = models.IntegerField()
    tabid = models.ForeignKey('VtigerTab', db_column='tabid')
    class Meta:
        managed = False
        db_table = 'vtiger_org_share_action2tab'

class VtigerOrgShareActionMapping(models.Model):
    share_action_id = models.IntegerField(primary_key=True)
    share_action_name = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_org_share_action_mapping'

class VtigerOrganizationdetails(models.Model):
    organizationname = models.CharField(unique=True, max_length=60)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    fax = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=100, blank=True)
    logoname = models.CharField(max_length=50, blank=True)
    logo = models.TextField(blank=True)
    organization_id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_organizationdetails'

class VtigerOrganizationdetailsSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_organizationdetails_seq'

class VtigerOwnernotify(models.Model):
    crmid = models.IntegerField(blank=True, null=True)
    smownerid = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_ownernotify'

class VtigerParenttab(models.Model):
    parenttabid = models.IntegerField(primary_key=True)
    parenttab_label = models.CharField(max_length=100)
    sequence = models.IntegerField()
    visible = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_parenttab'

class VtigerParenttabrel(models.Model):
    parenttabid = models.ForeignKey(VtigerParenttab, db_column='parenttabid')
    tabid = models.ForeignKey('VtigerTab', db_column='tabid')
    sequence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_parenttabrel'

class VtigerPaymentDuration(models.Model):
    payment_duration_id = models.IntegerField(blank=True, null=True)
    payment_duration = models.CharField(max_length=200, blank=True)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_payment_duration'

class VtigerPaymentDurationSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_payment_duration_seq'

class VtigerPbxmanager(models.Model):
    pbxmanagerid = models.IntegerField(blank=True, null=True)
    callfrom = models.CharField(max_length=255, blank=True)
    callto = models.CharField(max_length=255, blank=True)
    timeofcall = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_pbxmanager'

class VtigerPicklist(models.Model):
    picklistid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_picklist'

class VtigerPicklistDependency(models.Model):
    id = models.IntegerField(primary_key=True)
    tabid = models.IntegerField()
    sourcefield = models.CharField(max_length=255, blank=True)
    targetfield = models.CharField(max_length=255, blank=True)
    sourcevalue = models.CharField(max_length=100, blank=True)
    targetvalues = models.TextField(blank=True)
    criteria = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_picklist_dependency'

class VtigerPicklistDependencySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_picklist_dependency_seq'

class VtigerPicklistSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_picklist_seq'

class VtigerPicklistvaluesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_picklistvalues_seq'

class VtigerPobillads(models.Model):
    pobilladdressid = models.ForeignKey('VtigerPurchaseorder', db_column='pobilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True)
    bill_code = models.CharField(max_length=30, blank=True)
    bill_country = models.CharField(max_length=30, blank=True)
    bill_state = models.CharField(max_length=30, blank=True)
    bill_street = models.CharField(max_length=250, blank=True)
    bill_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_pobillads'

class VtigerPortal(models.Model):
    portalid = models.IntegerField(primary_key=True)
    portalname = models.CharField(max_length=200)
    portalurl = models.CharField(max_length=255)
    sequence = models.IntegerField()
    setdefault = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_portal'

class VtigerPortalSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_portal_seq'

class VtigerPortalinfo(models.Model):
    id = models.ForeignKey(VtigerContactdetails, db_column='id', primary_key=True)
    user_name = models.CharField(max_length=50, blank=True)
    user_password = models.CharField(max_length=30, blank=True)
    type = models.CharField(max_length=5, blank=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_portalinfo'

class VtigerPoshipads(models.Model):
    poshipaddressid = models.ForeignKey('VtigerPurchaseorder', db_column='poshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True)
    ship_code = models.CharField(max_length=30, blank=True)
    ship_country = models.CharField(max_length=30, blank=True)
    ship_state = models.CharField(max_length=30, blank=True)
    ship_street = models.CharField(max_length=250, blank=True)
    ship_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_poshipads'

class VtigerPostatus(models.Model):
    postatusid = models.IntegerField(primary_key=True)
    postatus = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_postatus'

class VtigerPostatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_postatus_seq'

class VtigerPostatushistory(models.Model):
    historyid = models.IntegerField(primary_key=True)
    purchaseorderid = models.ForeignKey('VtigerPurchaseorder', db_column='purchaseorderid')
    vendorname = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    postatus = models.CharField(max_length=200, blank=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_postatushistory'

class VtigerPotcompetitorrel(models.Model):
    potentialid = models.ForeignKey('VtigerPotential', db_column='potentialid')
    competitorid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_potcompetitorrel'

class VtigerPotential(models.Model):
    potentialid = models.ForeignKey(VtigerCrmentity, db_column='potentialid', primary_key=True)
    potential_no = models.CharField(max_length=100)
    related_to = models.IntegerField(blank=True, null=True)
    potentialname = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True)
    closingdate = models.DateField(blank=True, null=True)
    typeofrevenue = models.CharField(max_length=50, blank=True)
    nextstep = models.CharField(max_length=100, blank=True)
    private = models.IntegerField(blank=True, null=True)
    probability = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    campaignid = models.IntegerField(blank=True, null=True)
    sales_stage = models.CharField(max_length=200, blank=True)
    potentialtype = models.CharField(max_length=200, blank=True)
    leadsource = models.CharField(max_length=200, blank=True)
    productid = models.IntegerField(blank=True, null=True)
    productversion = models.CharField(max_length=50, blank=True)
    quotationref = models.CharField(max_length=50, blank=True)
    partnercontact = models.CharField(max_length=50, blank=True)
    remarks = models.CharField(max_length=50, blank=True)
    runtimefee = models.IntegerField(blank=True, null=True)
    followupdate = models.DateField(blank=True, null=True)
    evaluationstatus = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    forecastcategory = models.IntegerField(blank=True, null=True)
    outcomeanalysis = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_potential'

class VtigerPotentialscf(models.Model):
    potentialid = models.ForeignKey(VtigerPotential, db_column='potentialid', primary_key=True)
    cf_627 = models.CharField(max_length=50, blank=True)
    cf_726 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_potentialscf'

class VtigerPotstagehistory(models.Model):
    historyid = models.IntegerField(primary_key=True)
    potentialid = models.ForeignKey(VtigerPotential, db_column='potentialid')
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    stage = models.CharField(max_length=100, blank=True)
    probability = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    expectedrevenue = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    closedate = models.DateField(blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_potstagehistory'

class VtigerPricebook(models.Model):
    pricebookid = models.ForeignKey(VtigerCrmentity, db_column='pricebookid', primary_key=True)
    pricebook_no = models.CharField(max_length=100)
    bookname = models.CharField(max_length=100, blank=True)
    active = models.IntegerField(blank=True, null=True)
    currency_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_pricebook'

class VtigerPricebookcf(models.Model):
    pricebookid = models.ForeignKey(VtigerPricebook, db_column='pricebookid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_pricebookcf'

class VtigerPricebookproductrel(models.Model):
    pricebookid = models.ForeignKey(VtigerPricebook, db_column='pricebookid')
    productid = models.IntegerField()
    listprice = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    usedcurrency = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_pricebookproductrel'

class VtigerPriority(models.Model):
    priorityid = models.IntegerField(primary_key=True)
    priority = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_priority'

class VtigerProductcategory(models.Model):
    productcategoryid = models.IntegerField(primary_key=True)
    productcategory = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_productcategory'

class VtigerProductcategorySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_productcategory_seq'

class VtigerProductcf(models.Model):
    productid = models.ForeignKey('VtigerProducts', db_column='productid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_productcf'

class VtigerProductcollaterals(models.Model):
    productid = models.ForeignKey('VtigerProducts', db_column='productid', primary_key=True)
    date_entered = models.DateTimeField()
    data = models.TextField(blank=True)
    description = models.TextField(blank=True)
    filename = models.CharField(max_length=50, blank=True)
    filesize = models.CharField(max_length=50)
    filetype = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'vtiger_productcollaterals'

class VtigerProductcurrencyrel(models.Model):
    productid = models.IntegerField()
    currencyid = models.IntegerField()
    converted_price = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    actual_price = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_productcurrencyrel'

class VtigerProducts(models.Model):
    productid = models.ForeignKey(VtigerCrmentity, db_column='productid', primary_key=True)
    product_no = models.CharField(max_length=100)
    productname = models.CharField(max_length=50)
    productcode = models.CharField(max_length=40, blank=True)
    productcategory = models.CharField(max_length=200, blank=True)
    manufacturer = models.CharField(max_length=200, blank=True)
    qty_per_unit = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    pack_size = models.IntegerField(blank=True, null=True)
    sales_start_date = models.DateField(blank=True, null=True)
    sales_end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    cost_factor = models.IntegerField(blank=True, null=True)
    commissionrate = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    commissionmethod = models.CharField(max_length=50, blank=True)
    discontinued = models.IntegerField()
    usageunit = models.CharField(max_length=200, blank=True)
    reorderlevel = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=100, blank=True)
    taxclass = models.CharField(max_length=200, blank=True)
    mfr_part_no = models.CharField(max_length=200, blank=True)
    vendor_part_no = models.CharField(max_length=200, blank=True)
    serialno = models.CharField(max_length=200, blank=True)
    qtyinstock = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    productsheet = models.CharField(max_length=200, blank=True)
    qtyindemand = models.IntegerField(blank=True, null=True)
    glacct = models.CharField(max_length=200, blank=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    imagename = models.TextField(blank=True)
    currency_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_products'

class VtigerProducttaxrel(models.Model):
    productid = models.IntegerField()
    taxid = models.IntegerField()
    taxpercentage = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_producttaxrel'

class VtigerProfile(models.Model):
    profileid = models.IntegerField(primary_key=True)
    profilename = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_profile'

class VtigerProfile2Field(models.Model):
    profileid = models.IntegerField()
    tabid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField()
    visible = models.IntegerField(blank=True, null=True)
    readonly = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_profile2field'

class VtigerProfile2Globalpermissions(models.Model):
    profileid = models.ForeignKey(VtigerProfile, db_column='profileid')
    globalactionid = models.IntegerField()
    globalactionpermission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_profile2globalpermissions'

class VtigerProfile2Standardpermissions(models.Model):
    profileid = models.IntegerField()
    tabid = models.IntegerField()
    operation = models.IntegerField()
    permissions = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_profile2standardpermissions'

class VtigerProfile2Tab(models.Model):
    profileid = models.IntegerField(blank=True, null=True)
    tabid = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_profile2tab'

class VtigerProfile2Utility(models.Model):
    profileid = models.IntegerField()
    tabid = models.IntegerField()
    activityid = models.IntegerField()
    permission = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_profile2utility'

class VtigerProfileSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_profile_seq'

class VtigerProgress(models.Model):
    progressid = models.IntegerField(primary_key=True)
    progress = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_progress'

class VtigerProgressSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_progress_seq'

class VtigerProject(models.Model):
    projectid = models.IntegerField(blank=True, null=True)
    projectname = models.CharField(max_length=255, blank=True)
    project_no = models.CharField(max_length=100, blank=True)
    startdate = models.DateField(blank=True, null=True)
    targetenddate = models.DateField(blank=True, null=True)
    actualenddate = models.DateField(blank=True, null=True)
    targetbudget = models.CharField(max_length=255, blank=True)
    projecturl = models.CharField(max_length=255, blank=True)
    projectstatus = models.CharField(max_length=100, blank=True)
    projectpriority = models.CharField(max_length=100, blank=True)
    projecttype = models.CharField(max_length=100, blank=True)
    progress = models.CharField(max_length=100, blank=True)
    linktoaccountscontacts = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_project'

class VtigerProjectcf(models.Model):
    projectid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_projectcf'

class VtigerProjectmilestone(models.Model):
    projectmilestoneid = models.IntegerField(primary_key=True)
    projectmilestonename = models.CharField(max_length=255, blank=True)
    projectmilestone_no = models.CharField(max_length=100, blank=True)
    projectmilestonedate = models.CharField(max_length=255, blank=True)
    projectid = models.CharField(max_length=100, blank=True)
    projectmilestonetype = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_projectmilestone'

class VtigerProjectmilestonecf(models.Model):
    projectmilestoneid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_projectmilestonecf'

class VtigerProjectmilestonetype(models.Model):
    projectmilestonetypeid = models.IntegerField(primary_key=True)
    projectmilestonetype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projectmilestonetype'

class VtigerProjectmilestonetypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projectmilestonetype_seq'

class VtigerProjectpriority(models.Model):
    projectpriorityid = models.IntegerField(primary_key=True)
    projectpriority = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projectpriority'

class VtigerProjectprioritySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projectpriority_seq'

class VtigerProjectstatus(models.Model):
    projectstatusid = models.IntegerField(primary_key=True)
    projectstatus = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projectstatus'

class VtigerProjectstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projectstatus_seq'

class VtigerProjecttask(models.Model):
    projecttaskid = models.IntegerField(primary_key=True)
    projecttaskname = models.CharField(max_length=255, blank=True)
    projecttask_no = models.CharField(max_length=100, blank=True)
    projecttasktype = models.CharField(max_length=100, blank=True)
    projecttaskpriority = models.CharField(max_length=100, blank=True)
    projecttaskprogress = models.CharField(max_length=100, blank=True)
    projecttaskhours = models.CharField(max_length=255, blank=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    projectid = models.CharField(max_length=100, blank=True)
    projecttasknumber = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_projecttask'

class VtigerProjecttaskcf(models.Model):
    projecttaskid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_projecttaskcf'

class VtigerProjecttaskpriority(models.Model):
    projecttaskpriorityid = models.IntegerField(primary_key=True)
    projecttaskpriority = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttaskpriority'

class VtigerProjecttaskprioritySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttaskpriority_seq'

class VtigerProjecttaskprogress(models.Model):
    projecttaskprogressid = models.IntegerField(primary_key=True)
    projecttaskprogress = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttaskprogress'

class VtigerProjecttaskprogressSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttaskprogress_seq'

class VtigerProjecttasktype(models.Model):
    projecttasktypeid = models.IntegerField(primary_key=True)
    projecttasktype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttasktype'

class VtigerProjecttasktypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttasktype_seq'

class VtigerProjecttype(models.Model):
    projecttypeid = models.IntegerField(primary_key=True)
    projecttype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttype'

class VtigerProjecttypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_projecttype_seq'

class VtigerPurchaseorder(models.Model):
    purchaseorderid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100, blank=True)
    quoteid = models.IntegerField(blank=True, null=True)
    vendorid = models.ForeignKey('VtigerVendor', db_column='vendorid', blank=True, null=True)
    requisition_no = models.CharField(max_length=100, blank=True)
    purchaseorder_no = models.CharField(max_length=100, blank=True)
    tracking_no = models.CharField(max_length=100, blank=True)
    contactid = models.IntegerField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=100, blank=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    salescommission = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    exciseduty = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    terms_conditions = models.TextField(blank=True)
    postatus = models.CharField(max_length=200, blank=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    class Meta:
        managed = False
        db_table = 'vtiger_purchaseorder'

class VtigerPurchaseordercf(models.Model):
    purchaseorderid = models.ForeignKey(VtigerPurchaseorder, db_column='purchaseorderid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_purchaseordercf'

class VtigerQuickview(models.Model):
    fieldid = models.ForeignKey(VtigerField, db_column='fieldid')
    related_fieldid = models.IntegerField()
    sequence = models.IntegerField()
    currentview = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_quickview'

class VtigerQuotes(models.Model):
    quoteid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100, blank=True)
    potentialid = models.ForeignKey(VtigerPotential, db_column='potentialid', blank=True, null=True)
    quotestage = models.CharField(max_length=200, blank=True)
    validtill = models.DateField(blank=True, null=True)
    contactid = models.IntegerField(blank=True, null=True)
    quote_no = models.CharField(max_length=100, blank=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True)
    shipping = models.CharField(max_length=100, blank=True)
    inventorymanager = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    class Meta:
        managed = False
        db_table = 'vtiger_quotes'

class VtigerQuotesbillads(models.Model):
    quotebilladdressid = models.ForeignKey(VtigerQuotes, db_column='quotebilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True)
    bill_code = models.CharField(max_length=30, blank=True)
    bill_country = models.CharField(max_length=30, blank=True)
    bill_state = models.CharField(max_length=30, blank=True)
    bill_street = models.CharField(max_length=250, blank=True)
    bill_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_quotesbillads'

class VtigerQuotescf(models.Model):
    quoteid = models.ForeignKey(VtigerQuotes, db_column='quoteid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_quotescf'

class VtigerQuotesshipads(models.Model):
    quoteshipaddressid = models.ForeignKey(VtigerQuotes, db_column='quoteshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True)
    ship_code = models.CharField(max_length=30, blank=True)
    ship_country = models.CharField(max_length=30, blank=True)
    ship_state = models.CharField(max_length=30, blank=True)
    ship_street = models.CharField(max_length=250, blank=True)
    ship_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_quotesshipads'

class VtigerQuotestage(models.Model):
    quotestageid = models.IntegerField(primary_key=True)
    quotestage = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_quotestage'

class VtigerQuotestageSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_quotestage_seq'

class VtigerQuotestagehistory(models.Model):
    historyid = models.IntegerField(primary_key=True)
    quoteid = models.ForeignKey(VtigerQuotes, db_column='quoteid')
    accountname = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    quotestage = models.CharField(max_length=200, blank=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_quotestagehistory'

class VtigerRating(models.Model):
    rating_id = models.IntegerField(primary_key=True)
    rating = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_rating'

class VtigerRatingSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_rating_seq'

class VtigerRecurringFrequency(models.Model):
    recurring_frequency_id = models.IntegerField(blank=True, null=True)
    recurring_frequency = models.CharField(max_length=200, blank=True)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_recurring_frequency'

class VtigerRecurringFrequencySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_recurring_frequency_seq'

class VtigerRecurringevents(models.Model):
    recurringid = models.IntegerField(primary_key=True)
    activityid = models.ForeignKey(VtigerActivity, db_column='activityid')
    recurringdate = models.DateField(blank=True, null=True)
    recurringtype = models.CharField(max_length=30, blank=True)
    recurringfreq = models.IntegerField(blank=True, null=True)
    recurringinfo = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_recurringevents'

class VtigerRecurringtype(models.Model):
    recurringeventid = models.IntegerField(primary_key=True)
    recurringtype = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_recurringtype'

class VtigerRecurringtypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_recurringtype_seq'

class VtigerRelatedlists(models.Model):
    relation_id = models.IntegerField()
    tabid = models.IntegerField(blank=True, null=True)
    related_tabid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=100, blank=True)
    presence = models.IntegerField()
    actions = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'vtiger_relatedlists'

class VtigerRelatedlistsRb(models.Model):
    entityid = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True)
    rel_table = models.CharField(max_length=200, blank=True)
    rel_column = models.CharField(max_length=200, blank=True)
    ref_column = models.CharField(max_length=200, blank=True)
    related_crm_ids = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_relatedlists_rb'

class VtigerRelatedlistsSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_relatedlists_seq'

class VtigerRelcriteria(models.Model):
    queryid = models.ForeignKey('VtigerSelectquery', db_column='queryid')
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True)
    comparator = models.CharField(max_length=10, blank=True)
    value = models.CharField(max_length=200, blank=True)
    groupid = models.IntegerField(blank=True, null=True)
    column_condition = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_relcriteria'

class VtigerRelcriteriaGrouping(models.Model):
    groupid = models.IntegerField()
    queryid = models.IntegerField()
    group_condition = models.CharField(max_length=256, blank=True)
    condition_expression = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_relcriteria_grouping'

class VtigerReminderInterval(models.Model):
    reminder_intervalid = models.IntegerField(primary_key=True)
    reminder_interval = models.CharField(max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_reminder_interval'

class VtigerReminderIntervalSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_reminder_interval_seq'

class VtigerReport(models.Model):
    reportid = models.IntegerField(primary_key=True)
    folderid = models.IntegerField()
    reportname = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250, blank=True)
    reporttype = models.CharField(max_length=50, blank=True)
    queryid = models.ForeignKey('VtigerSelectquery', db_column='queryid')
    state = models.CharField(max_length=50, blank=True)
    customizable = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    sharingtype = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_report'

class VtigerReportdatefilter(models.Model):
    datefilterid = models.ForeignKey(VtigerReport, db_column='datefilterid')
    datecolumnname = models.CharField(max_length=250, blank=True)
    datefilter = models.CharField(max_length=250, blank=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_reportdatefilter'

class VtigerReportfilters(models.Model):
    filterid = models.IntegerField()
    name = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_reportfilters'

class VtigerReportfolder(models.Model):
    folderid = models.IntegerField(primary_key=True)
    foldername = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_reportfolder'

class VtigerReportgroupbycolumn(models.Model):
    reportid = models.IntegerField(blank=True, null=True)
    sortid = models.IntegerField(blank=True, null=True)
    sortcolname = models.CharField(max_length=250, blank=True)
    dategroupbycriteria = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_reportgroupbycolumn'

class VtigerReportmodules(models.Model):
    reportmodulesid = models.ForeignKey(VtigerReport, db_column='reportmodulesid', primary_key=True)
    primarymodule = models.CharField(max_length=50)
    secondarymodules = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_reportmodules'

class VtigerReportsharing(models.Model):
    reportid = models.IntegerField()
    shareid = models.IntegerField()
    setype = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_reportsharing'

class VtigerReportsortcol(models.Model):
    sortcolid = models.IntegerField()
    reportid = models.ForeignKey(VtigerReport, db_column='reportid')
    columnname = models.CharField(max_length=250, blank=True)
    sortorder = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_reportsortcol'

class VtigerReportsummary(models.Model):
    reportsummaryid = models.ForeignKey(VtigerReport, db_column='reportsummaryid')
    summarytype = models.IntegerField()
    columnname = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'vtiger_reportsummary'

class VtigerRevenuetype(models.Model):
    revenuetypeid = models.IntegerField(primary_key=True)
    revenuetype = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_revenuetype'

class VtigerRole(models.Model):
    roleid = models.CharField(primary_key=True, max_length=255)
    rolename = models.CharField(max_length=200, blank=True)
    parentrole = models.CharField(max_length=255, blank=True)
    depth = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_role'

class VtigerRole2Picklist(models.Model):
    roleid = models.ForeignKey(VtigerRole, db_column='roleid')
    picklistvalueid = models.IntegerField()
    picklistid = models.ForeignKey(VtigerPicklist, db_column='picklistid')
    sortid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_role2picklist'

class VtigerRole2Profile(models.Model):
    roleid = models.CharField(max_length=255)
    profileid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_role2profile'

class VtigerRoleSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_role_seq'

class VtigerRss(models.Model):
    rssid = models.IntegerField(primary_key=True)
    rssurl = models.CharField(max_length=200)
    rsstitle = models.CharField(max_length=200, blank=True)
    rsstype = models.IntegerField(blank=True, null=True)
    starred = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_rss'

class VtigerSalesStage(models.Model):
    sales_stage_id = models.IntegerField(primary_key=True)
    sales_stage = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_sales_stage'

class VtigerSalesStageSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_sales_stage_seq'

class VtigerSalesmanactivityrel(models.Model):
    smid = models.ForeignKey('VtigerUsers', db_column='smid')
    activityid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_salesmanactivityrel'

class VtigerSalesmanattachmentsrel(models.Model):
    smid = models.IntegerField()
    attachmentsid = models.ForeignKey(VtigerAttachments, db_column='attachmentsid')
    class Meta:
        managed = False
        db_table = 'vtiger_salesmanattachmentsrel'

class VtigerSalesmanticketrel(models.Model):
    smid = models.ForeignKey('VtigerUsers', db_column='smid')
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_salesmanticketrel'

class VtigerSalesorder(models.Model):
    salesorderid = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100, blank=True)
    potentialid = models.IntegerField(blank=True, null=True)
    customerno = models.CharField(max_length=100, blank=True)
    salesorder_no = models.CharField(max_length=100, blank=True)
    quoteid = models.IntegerField(blank=True, null=True)
    vendorterms = models.CharField(max_length=100, blank=True)
    contactid = models.IntegerField(blank=True, null=True)
    vendorid = models.ForeignKey('VtigerVendor', db_column='vendorid', blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True)
    pending = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=100, blank=True)
    adjustment = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    salescommission = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    exciseduty = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    taxtype = models.CharField(max_length=25, blank=True)
    discount_percent = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    s_h_amount = models.DecimalField(max_digits=25, decimal_places=3, blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True)
    purchaseorder = models.CharField(max_length=200, blank=True)
    sostatus = models.CharField(max_length=200, blank=True)
    currency_id = models.IntegerField()
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=3)
    enable_recurring = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_salesorder'

class VtigerSalesordercf(models.Model):
    salesorderid = models.ForeignKey(VtigerSalesorder, db_column='salesorderid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_salesordercf'

class VtigerSalutationtype(models.Model):
    salutationid = models.IntegerField(primary_key=True)
    salutationtype = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_salutationtype'

class VtigerSalutationtypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_salutationtype_seq'

class VtigerScheduledReports(models.Model):
    reportid = models.IntegerField(primary_key=True)
    recipients = models.TextField(blank=True)
    schedule = models.TextField(blank=True)
    format = models.CharField(max_length=10, blank=True)
    next_trigger_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'vtiger_scheduled_reports'

class VtigerSeactivityrel(models.Model):
    crmid = models.ForeignKey(VtigerCrmentity, db_column='crmid')
    activityid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_seactivityrel'

class VtigerSeactivityrelSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_seactivityrel_seq'

class VtigerSeattachmentsrel(models.Model):
    crmid = models.ForeignKey(VtigerCrmentity, db_column='crmid')
    attachmentsid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_seattachmentsrel'

class VtigerSelectcolumn(models.Model):
    queryid = models.ForeignKey('VtigerSelectquery', db_column='queryid')
    columnindex = models.IntegerField()
    columnname = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_selectcolumn'

class VtigerSelectquery(models.Model):
    queryid = models.IntegerField()
    startindex = models.IntegerField(blank=True, null=True)
    numofobjects = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_selectquery'

class VtigerSelectquerySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_selectquery_seq'

class VtigerSenotesrel(models.Model):
    crmid = models.IntegerField()
    notesid = models.ForeignKey(VtigerNotes, db_column='notesid')
    class Meta:
        managed = False
        db_table = 'vtiger_senotesrel'

class VtigerSeproductsrel(models.Model):
    crmid = models.IntegerField()
    productid = models.ForeignKey(VtigerProducts, db_column='productid')
    setype = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'vtiger_seproductsrel'

class VtigerService(models.Model):
    serviceid = models.ForeignKey(VtigerCrmentity, db_column='serviceid', primary_key=True)
    service_no = models.CharField(max_length=100)
    servicename = models.CharField(max_length=50)
    servicecategory = models.CharField(max_length=200, blank=True)
    qty_per_unit = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    sales_start_date = models.DateField(blank=True, null=True)
    sales_end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    discontinued = models.IntegerField()
    service_usageunit = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=100, blank=True)
    taxclass = models.CharField(max_length=200, blank=True)
    currency_id = models.IntegerField()
    commissionrate = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_service'

class VtigerServiceUsageunit(models.Model):
    service_usageunitid = models.IntegerField(primary_key=True)
    service_usageunit = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_service_usageunit'

class VtigerServiceUsageunitSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_service_usageunit_seq'

class VtigerServicecategory(models.Model):
    servicecategoryid = models.IntegerField(primary_key=True)
    servicecategory = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_servicecategory'

class VtigerServicecategorySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_servicecategory_seq'

class VtigerServicecf(models.Model):
    serviceid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_servicecf'

class VtigerServicecontracts(models.Model):
    servicecontractsid = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    sc_related_to = models.IntegerField(blank=True, null=True)
    tracking_unit = models.CharField(max_length=100, blank=True)
    total_units = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    used_units = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True)
    due_date = models.DateField(blank=True, null=True)
    planned_duration = models.CharField(max_length=256, blank=True)
    actual_duration = models.CharField(max_length=256, blank=True)
    contract_status = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=200, blank=True)
    contract_type = models.CharField(max_length=200, blank=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    contract_no = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_servicecontracts'

class VtigerServicecontractscf(models.Model):
    servicecontractsid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_servicecontractscf'

class VtigerSeticketsrel(models.Model):
    crmid = models.IntegerField()
    ticketid = models.ForeignKey('VtigerTroubletickets', db_column='ticketid')
    class Meta:
        managed = False
        db_table = 'vtiger_seticketsrel'

class VtigerSettingsBlocks(models.Model):
    blockid = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=250, blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_settings_blocks'

class VtigerSettingsBlocksSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_settings_blocks_seq'

class VtigerSettingsField(models.Model):
    fieldid = models.IntegerField(primary_key=True)
    blockid = models.ForeignKey(VtigerSettingsBlocks, db_column='blockid', blank=True, null=True)
    name = models.CharField(max_length=250, blank=True)
    iconpath = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    linkto = models.TextField(blank=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_settings_field'

class VtigerSettingsFieldSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_settings_field_seq'

class VtigerSharedcalendar(models.Model):
    userid = models.IntegerField()
    sharedid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_sharedcalendar'

class VtigerShippingtaxinfo(models.Model):
    taxid = models.IntegerField(primary_key=True)
    taxname = models.CharField(max_length=50, blank=True)
    taxlabel = models.CharField(max_length=50, blank=True)
    percentage = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_shippingtaxinfo'

class VtigerShippingtaxinfoSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_shippingtaxinfo_seq'

class VtigerSmsnotifier(models.Model):
    smsnotifierid = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_smsnotifier'

class VtigerSmsnotifierServers(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=255, blank=True)
    isactive = models.IntegerField(blank=True, null=True)
    providertype = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=255, blank=True)
    parameters = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_smsnotifier_servers'

class VtigerSmsnotifierStatus(models.Model):
    smsnotifierid = models.IntegerField(blank=True, null=True)
    tonumber = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, blank=True)
    smsmessageid = models.CharField(max_length=50, blank=True)
    needlookup = models.IntegerField(blank=True, null=True)
    statusid = models.IntegerField(primary_key=True)
    statusmessage = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_smsnotifier_status'

class VtigerSmsnotifiercf(models.Model):
    smsnotifierid = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_smsnotifiercf'

class VtigerSoapservice(models.Model):
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=25, blank=True)
    sessionid = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_soapservice'

class VtigerSobillads(models.Model):
    sobilladdressid = models.ForeignKey(VtigerSalesorder, db_column='sobilladdressid', primary_key=True)
    bill_city = models.CharField(max_length=30, blank=True)
    bill_code = models.CharField(max_length=30, blank=True)
    bill_country = models.CharField(max_length=30, blank=True)
    bill_state = models.CharField(max_length=30, blank=True)
    bill_street = models.CharField(max_length=250, blank=True)
    bill_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_sobillads'

class VtigerSoshipads(models.Model):
    soshipaddressid = models.ForeignKey(VtigerSalesorder, db_column='soshipaddressid', primary_key=True)
    ship_city = models.CharField(max_length=30, blank=True)
    ship_code = models.CharField(max_length=30, blank=True)
    ship_country = models.CharField(max_length=30, blank=True)
    ship_state = models.CharField(max_length=30, blank=True)
    ship_street = models.CharField(max_length=250, blank=True)
    ship_pobox = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_soshipads'

class VtigerSostatus(models.Model):
    sostatusid = models.IntegerField(primary_key=True)
    sostatus = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_sostatus'

class VtigerSostatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_sostatus_seq'

class VtigerSostatushistory(models.Model):
    historyid = models.IntegerField(primary_key=True)
    salesorderid = models.ForeignKey(VtigerSalesorder, db_column='salesorderid')
    accountname = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sostatus = models.CharField(max_length=200, blank=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_sostatushistory'

class VtigerStatus(models.Model):
    statusid = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_status'

class VtigerStatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_status_seq'

class VtigerSystems(models.Model):
    id = models.IntegerField(primary_key=True)
    server = models.CharField(max_length=100, blank=True)
    server_port = models.IntegerField(blank=True, null=True)
    server_username = models.CharField(max_length=100, blank=True)
    server_password = models.CharField(max_length=100, blank=True)
    server_type = models.CharField(max_length=20, blank=True)
    smtp_auth = models.CharField(max_length=5, blank=True)
    server_path = models.CharField(max_length=256, blank=True)
    from_email_field = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_systems'

class VtigerSystemsSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_systems_seq'

class VtigerTab(models.Model):
    tabid = models.IntegerField()
    name = models.CharField(unique=True, max_length=25)
    presence = models.IntegerField()
    tabsequence = models.IntegerField(blank=True, null=True)
    tablabel = models.CharField(max_length=25)
    modifiedby = models.IntegerField(blank=True, null=True)
    modifiedtime = models.IntegerField(blank=True, null=True)
    customized = models.IntegerField(blank=True, null=True)
    ownedby = models.IntegerField(blank=True, null=True)
    isentitytype = models.IntegerField()
    version = models.CharField(max_length=10, blank=True)
    parent = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_tab'

class VtigerTabInfo(models.Model):
    tabid = models.ForeignKey(VtigerTab, db_column='tabid', blank=True, null=True)
    prefname = models.CharField(max_length=256, blank=True)
    prefvalue = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_tab_info'

class VtigerTaskpriority(models.Model):
    taskpriorityid = models.IntegerField(primary_key=True)
    taskpriority = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_taskpriority'

class VtigerTaskprioritySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_taskpriority_seq'

class VtigerTaskstatus(models.Model):
    taskstatusid = models.IntegerField(primary_key=True)
    taskstatus = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_taskstatus'

class VtigerTaskstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_taskstatus_seq'

class VtigerTaxclass(models.Model):
    taxclassid = models.IntegerField(primary_key=True)
    taxclass = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_taxclass'

class VtigerTaxclassSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_taxclass_seq'

class VtigerTicketcategories(models.Model):
    ticketcategories_id = models.IntegerField(primary_key=True)
    ticketcategories = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketcategories'

class VtigerTicketcategoriesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketcategories_seq'

class VtigerTicketcf(models.Model):
    ticketid = models.ForeignKey('VtigerTroubletickets', db_column='ticketid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_ticketcf'

class VtigerTicketcomments(models.Model):
    commentid = models.IntegerField(primary_key=True)
    ticketid = models.ForeignKey('VtigerTroubletickets', db_column='ticketid', blank=True, null=True)
    comments = models.TextField(blank=True)
    ownerid = models.IntegerField()
    ownertype = models.CharField(max_length=10, blank=True)
    createdtime = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketcomments'

class VtigerTicketpriorities(models.Model):
    ticketpriorities_id = models.IntegerField(primary_key=True)
    ticketpriorities = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketpriorities'

class VtigerTicketprioritiesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketpriorities_seq'

class VtigerTicketseverities(models.Model):
    ticketseverities_id = models.IntegerField(primary_key=True)
    ticketseverities = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketseverities'

class VtigerTicketseveritiesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketseverities_seq'

class VtigerTicketstatus(models.Model):
    ticketstatus_id = models.IntegerField(primary_key=True)
    ticketstatus = models.CharField(max_length=200, blank=True)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketstatus'

class VtigerTicketstatusSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketstatus_seq'

class VtigerTicketstracktime(models.Model):
    ticket_id = models.IntegerField()
    supporter_id = models.IntegerField()
    minutes = models.IntegerField(blank=True, null=True)
    date_logged = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ticketstracktime'

class VtigerTimeZone(models.Model):
    time_zoneid = models.IntegerField(primary_key=True)
    time_zone = models.CharField(max_length=200)
    sortorderid = models.IntegerField(blank=True, null=True)
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_time_zone'

class VtigerTimeZoneSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_time_zone_seq'

class VtigerTmpReadGroupRelSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    sharedgroupid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_read_group_rel_sharing_per'

class VtigerTmpReadGroupSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    sharedgroupid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_read_group_sharing_per'

class VtigerTmpReadUserRelSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    shareduserid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_read_user_rel_sharing_per'

class VtigerTmpReadUserSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    shareduserid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_read_user_sharing_per'

class VtigerTmpWriteGroupRelSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    sharedgroupid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_write_group_rel_sharing_per'

class VtigerTmpWriteGroupSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    sharedgroupid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_write_group_sharing_per'

class VtigerTmpWriteUserRelSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    relatedtabid = models.IntegerField()
    shareduserid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_write_user_rel_sharing_per'

class VtigerTmpWriteUserSharingPer(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid')
    tabid = models.IntegerField()
    shareduserid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tmp_write_user_sharing_per'

class VtigerTracker(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=36, blank=True)
    module_name = models.CharField(max_length=25, blank=True)
    item_id = models.CharField(max_length=36, blank=True)
    item_summary = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_tracker'

class VtigerTrackingUnit(models.Model):
    tracking_unitid = models.IntegerField(primary_key=True)
    tracking_unit = models.CharField(max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tracking_unit'

class VtigerTrackingUnitSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_tracking_unit_seq'

class VtigerTroubletickets(models.Model):
    ticketid = models.ForeignKey(VtigerCrmentity, db_column='ticketid')
    ticket_no = models.CharField(max_length=100)
    groupname = models.CharField(max_length=100, blank=True)
    parent_id = models.CharField(max_length=100, blank=True)
    product_id = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=200, blank=True)
    severity = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255)
    solution = models.TextField(blank=True)
    update_log = models.TextField(blank=True)
    version_id = models.IntegerField(blank=True, null=True)
    hours = models.CharField(max_length=200, blank=True)
    days = models.CharField(max_length=200, blank=True)
    from_portal = models.CharField(max_length=3, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_troubletickets'

class VtigerUsageunit(models.Model):
    usageunitid = models.IntegerField(primary_key=True)
    usageunit = models.CharField(unique=True, max_length=200)
    presence = models.IntegerField()
    picklist_valueid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_usageunit'

class VtigerUsageunitSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_usageunit_seq'

class VtigerUser2Mergefields(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    tabid = models.IntegerField(blank=True, null=True)
    fieldid = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_user2mergefields'

class VtigerUser2Role(models.Model):
    userid = models.ForeignKey('VtigerUsers', db_column='userid', primary_key=True)
    roleid = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'vtiger_user2role'

class VtigerUserModulePreferences(models.Model):
    userid = models.IntegerField()
    tabid = models.ForeignKey(VtigerTab, db_column='tabid')
    default_cvid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_user_module_preferences'

class VtigerUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True)
    user_password = models.CharField(max_length=200, blank=True)
    user_hash = models.CharField(max_length=32, blank=True)
    cal_color = models.CharField(max_length=25, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
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

class VtigerUsers2Group(models.Model):
    groupid = models.IntegerField()
    userid = models.ForeignKey(VtigerUsers, db_column='userid')
    class Meta:
        managed = False
        db_table = 'vtiger_users2group'

class VtigerUsersLastImport(models.Model):
    id = models.IntegerField(primary_key=True)
    assigned_user_id = models.CharField(max_length=36, blank=True)
    bean_type = models.CharField(max_length=36, blank=True)
    bean_id = models.CharField(max_length=36, blank=True)
    deleted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_users_last_import'

class VtigerUsersSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_users_seq'

class VtigerUsertype(models.Model):
    usertypeid = models.IntegerField(primary_key=True)
    usertype = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_usertype'

class VtigerVendor(models.Model):
    vendorid = models.ForeignKey(VtigerCrmentity, db_column='vendorid', primary_key=True)
    vendor_no = models.CharField(max_length=100)
    vendorname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    glacct = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, blank=True)
    street = models.TextField(blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    pobox = models.CharField(max_length=30, blank=True)
    postalcode = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_vendor'

class VtigerVendorcf(models.Model):
    vendorid = models.ForeignKey(VtigerVendor, db_column='vendorid', primary_key=True)
    class Meta:
        managed = False
        db_table = 'vtiger_vendorcf'

class VtigerVendorcontactrel(models.Model):
    vendorid = models.ForeignKey(VtigerVendor, db_column='vendorid')
    contactid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_vendorcontactrel'

class VtigerVersion(models.Model):
    id = models.IntegerField(primary_key=True)
    old_version = models.CharField(max_length=30, blank=True)
    current_version = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_version'

class VtigerVersionSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_version_seq'

class VtigerVisibility(models.Model):
    visibilityid = models.IntegerField(primary_key=True)
    visibility = models.CharField(unique=True, max_length=200)
    sortorderid = models.IntegerField()
    presence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_visibility'

class VtigerVisibilitySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_visibility_seq'

class VtigerWebforms(models.Model):
    id = models.IntegerField()
    name = models.CharField(unique=True, max_length=100)
    publicid = models.CharField(max_length=100)
    enabled = models.IntegerField()
    targetmodule = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    ownerid = models.IntegerField()
    returnurl = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_webforms'

class VtigerWebformsArchive(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    insert_timestamp = models.DateTimeField()
    leadsource = models.TextField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    traffic_source = models.TextField(blank=True)
    cookie = models.TextField(blank=True)
    keyword = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_webforms_archive'

class VtigerWebformsField(models.Model):
    id = models.IntegerField()
    webformid = models.ForeignKey(VtigerWebforms, db_column='webformid')
    fieldname = models.ForeignKey(VtigerField, db_column='fieldname')
    neutralizedfield = models.CharField(max_length=50)
    defaultvalue = models.CharField(max_length=200, blank=True)
    required = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_webforms_field'

class VtigerWordtemplates(models.Model):
    templateid = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=100)
    module = models.CharField(max_length=30)
    date_entered = models.DateTimeField()
    parent_type = models.CharField(max_length=50)
    data = models.TextField(blank=True)
    description = models.TextField(blank=True)
    filesize = models.CharField(max_length=50)
    filetype = models.CharField(max_length=20)
    deleted = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_wordtemplates'

class VtigerWordtemplatesSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_wordtemplates_seq'

class VtigerWsEntity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    handler_path = models.CharField(max_length=255)
    handler_class = models.CharField(max_length=64)
    ismodule = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity'

class VtigerWsEntityFieldtype(models.Model):
    fieldtypeid = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
    fieldtype = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity_fieldtype'

class VtigerWsEntityFieldtypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity_fieldtype_seq'

class VtigerWsEntityName(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    name_fields = models.CharField(max_length=50)
    index_field = models.CharField(max_length=50)
    table_name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity_name'

class VtigerWsEntityReferencetype(models.Model):
    fieldtypeid = models.ForeignKey(VtigerWsEntityFieldtype, db_column='fieldtypeid')
    type = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity_referencetype'

class VtigerWsEntitySeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity_seq'

class VtigerWsEntityTables(models.Model):
    webservice_entity = models.ForeignKey(VtigerWsEntity)
    table_name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_entity_tables'

class VtigerWsFieldinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    property_name = models.CharField(max_length=32, blank=True)
    property_value = models.CharField(max_length=64, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_fieldinfo'

class VtigerWsFieldtype(models.Model):
    fieldtypeid = models.IntegerField(primary_key=True)
    uitype = models.CharField(unique=True, max_length=30)
    fieldtype = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_fieldtype'

class VtigerWsFieldtypeSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_fieldtype_seq'

class VtigerWsOperation(models.Model):
    operationid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    handler_path = models.CharField(max_length=255)
    handler_method = models.CharField(max_length=64)
    type = models.CharField(max_length=8)
    prelogin = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_operation'

class VtigerWsOperationParameters(models.Model):
    operationid = models.IntegerField()
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    sequence = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_operation_parameters'

class VtigerWsOperationSeq(models.Model):
    id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_operation_seq'

class VtigerWsReferencetype(models.Model):
    fieldtypeid = models.ForeignKey(VtigerWsFieldtype, db_column='fieldtypeid')
    type = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'vtiger_ws_referencetype'

class VtigerWsUserauthtoken(models.Model):
    userid = models.IntegerField(unique=True)
    token = models.CharField(max_length=36)
    expiretime = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vtiger_ws_userauthtoken'

class VtigerWsapp(models.Model):
    appid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    appkey = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_wsapp'

class VtigerWsappHandlerdetails(models.Model):
    type = models.CharField(max_length=200)
    handlerclass = models.CharField(max_length=100, blank=True)
    handlerpath = models.CharField(max_length=300, blank=True)
    class Meta:
        managed = False
        db_table = 'vtiger_wsapp_handlerdetails'

class VtigerWsappQueuerecords(models.Model):
    syncserverid = models.IntegerField(blank=True, null=True)
    details = models.CharField(max_length=300, blank=True)
    flag = models.CharField(max_length=100, blank=True)
    appid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_wsapp_queuerecords'

class VtigerWsappRecordmapping(models.Model):
    id = models.IntegerField(primary_key=True)
    serverid = models.CharField(max_length=10, blank=True)
    clientid = models.CharField(max_length=255, blank=True)
    clientmodifiedtime = models.DateTimeField(blank=True, null=True)
    appid = models.IntegerField(blank=True, null=True)
    servermodifiedtime = models.DateTimeField(blank=True, null=True)
    serverappid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_wsapp_recordmapping'

class VtigerWsappSyncState(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    stateencodedvalues = models.CharField(max_length=300)
    userid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtiger_wsapp_sync_state'

