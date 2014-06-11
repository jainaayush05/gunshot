# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'reports_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('linenos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('language', self.gf('django.db.models.fields.CharField')(default='python', max_length=100)),
            ('style', self.gf('django.db.models.fields.CharField')(default='friendly', max_length=100)),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding model 'VtigerLeaddetails'
        db.create_table('vtiger_leaddetails', (
            ('leadid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('lead_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('interest', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('salutation', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('annualrevenue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('campaign', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('leadstatus', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('leadsource', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('converted', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('licencekeystatus', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('space', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('demorequest', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('partnercontact', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('productversion', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('maildate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('nextstepdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fundingsituation', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('evaluationstatus', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('transferdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('revenuetype', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('noofemployees', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('secondaryemail', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('assignleadchk', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['VtigerLeaddetails'])

        # Adding model 'VtigerLeadaddress'
        db.create_table('vtiger_leadaddress', (
            ('leadaddressid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('pobox', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('lane', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('leadaddresstype', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'reports', ['VtigerLeadaddress'])

        # Adding model 'VtigerLeadscf'
        db.create_table('vtiger_leadscf', (
            ('leadid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('cf_607', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('cf_609', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('cf_625', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cf_630', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('cf_632', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('cf_633', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_634', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=0, blank=True)),
            ('cf_636', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cf_637', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_638', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_639', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_640', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_677', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_678', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('cf_679', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('cf_689', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_690', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_691', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_694', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('cf_696', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cf_704', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=0, blank=True)),
            ('cf_706', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=0, blank=True)),
            ('cf_707', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_708', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_709', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_710', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_711', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=0, blank=True)),
            ('cf_712', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=0, blank=True)),
            ('cf_721', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_722', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_723', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cf_724', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_725', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=0, blank=True)),
            ('cf_727', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=0, blank=True)),
            ('cf_729', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cf_733', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'reports', ['VtigerLeadscf'])

        # Adding model 'GsRptFunnel'
        db.create_table('gs_rpt_funnel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('leadid', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('pobox', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('assgn_first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('assgn_last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('smownerid', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdtime', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('modifiedtime', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('lead_no', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('leadstatus', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('leadsource', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('campaign_id', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('google_keyword', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('ref_domain', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('traffic_src', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('google_cookie', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('verified', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('has_multiple_leads', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'reports', ['GsRptFunnel'])

        # Adding model 'VtigerGroups'
        db.create_table('vtiger_groups', (
            ('groupid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('groupname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'reports', ['VtigerGroups'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Deleting model 'VtigerLeaddetails'
        db.delete_table('vtiger_leaddetails')

        # Deleting model 'VtigerLeadaddress'
        db.delete_table('vtiger_leadaddress')

        # Deleting model 'VtigerLeadscf'
        db.delete_table('vtiger_leadscf')

        # Deleting model 'GsRptFunnel'
        db.delete_table('gs_rpt_funnel')

        # Deleting model 'VtigerGroups'
        db.delete_table('vtiger_groups')


    models = {
        u'reports.gsrptfunnel': {
            'Meta': {'object_name': 'GsRptFunnel', 'db_table': "'gs_rpt_funnel'"},
            'assgn_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'assgn_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'campaign_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'createdtime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'google_cookie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'google_keyword': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'has_multiple_leads': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'lead_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'leadid': ('django.db.models.fields.IntegerField', [], {}),
            'leadsource': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'leadstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modifiedtime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pobox': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ref_domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'smownerid': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'traffic_src': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'verified': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'reports.report': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Report'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'python'", 'max_length': '100'}),
            'linenos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'friendly'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        },
        u'reports.vtigercrmentity': {
            'Meta': {'object_name': 'VtigerCrmentity', 'db_table': "'vtiger_crmentity'", 'managed': 'False'},
            'createdtime': ('django.db.models.fields.DateTimeField', [], {}),
            'crmid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modifiedby': ('django.db.models.fields.IntegerField', [], {}),
            'modifiedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'presence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'setype': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'smcreatorid': ('django.db.models.fields.IntegerField', [], {}),
            'smownerid': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {}),
            'viewedtime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reports.vtigergroups': {
            'Meta': {'object_name': 'VtigerGroups', 'db_table': "'vtiger_groups'"},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'groupid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'groupname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'})
        },
        u'reports.vtigerleadaddress': {
            'Meta': {'object_name': 'VtigerLeadaddress', 'db_table': "'vtiger_leadaddress'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'lane': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'leadaddressid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'leadaddresstype': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pobox': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'reports.vtigerleaddetails': {
            'Meta': {'object_name': 'VtigerLeaddetails', 'db_table': "'vtiger_leaddetails'"},
            'annualrevenue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'assignleadchk': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'converted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'demorequest': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'evaluationstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'fundingsituation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'interest': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'lead_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'leadid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'leadsource': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'leadstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'licencekeystatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'maildate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nextstepdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'noofemployees': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'partnercontact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'productversion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'revenuetype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'secondaryemail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'space': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'transferdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reports.vtigerleadscf': {
            'Meta': {'object_name': 'VtigerLeadscf', 'db_table': "'vtiger_leadscf'"},
            'cf_607': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'cf_609': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'cf_625': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cf_630': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'cf_632': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'cf_633': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_634': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '0', 'blank': 'True'}),
            'cf_636': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cf_637': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_638': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_639': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_640': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_677': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_678': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'cf_679': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'cf_689': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_690': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_691': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_694': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'cf_696': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'cf_704': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '0', 'blank': 'True'}),
            'cf_706': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '0', 'blank': 'True'}),
            'cf_707': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_708': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_709': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_710': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_711': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '0', 'blank': 'True'}),
            'cf_712': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '0', 'blank': 'True'}),
            'cf_721': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_722': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_723': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cf_724': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_725': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'cf_727': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '0', 'blank': 'True'}),
            'cf_729': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cf_733': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'leadid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'reports.vtigerusers': {
            'Meta': {'object_name': 'VtigerUsers', 'db_table': "'vtiger_users'", 'managed': 'False'},
            'accesskey': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'activity_view': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_country': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'address_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'cal_color': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'confirm_password': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'crypt_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'currency_decimal_separator': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'currency_grouping_pattern': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'currency_grouping_separator': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'currency_id': ('django.db.models.fields.IntegerField', [], {}),
            'currency_symbol_placement': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date_entered': ('django.db.models.fields.DateTimeField', [], {}),
            'date_format': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'deleted': ('django.db.models.fields.IntegerField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'end_hour': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'holidays': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'hour_format': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagename': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'internal_mailer': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'is_admin': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lead_view': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'modified_user_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'namedays': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'phone_fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone_other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'reminder_interval': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'reminder_next_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'reports_to_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'secondaryemail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'start_hour': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tz': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user_hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user_password': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user_preferences': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'weekstart': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'workdays': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['reports']