from django.conf.urls import patterns, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from modules.authentication import views as authenticationViews
from modules.dashboard import views as dashboardViews
from modules.funnelReport import views as funnelReportViews
from modules.gunshot import views as gunshotViews
from modules.login import views as loginViews
from modules.logout import views as logoutViews
from modules.mailReport import views as mailReportViews
from modules.printReport import views as printReportViews
from modules.salesReport import views as salesReportViews
from modules.transactions import views as transactionsViews
from modules.vtigerCrm import views as vtigerCrmViews


urlpatterns = patterns('',
    url(r'^authentication/$', authenticationViews.Authentication.as_view()),
    url(r'^login/$', loginViews.Login.as_view()),
    url(r'^$', dashboardViews.Dashboard.as_view()),
    url(r'^logout/$', logoutViews.Logout.as_view()),
    url(r'^transactions/$', transactionsViews.Transactions.as_view()),
    url(r'^create_lead/$', gunshotViews.CreateLead.as_view()),
    url(r'^dashboard/$', dashboardViews.Dashboard.as_view()),
    url(r'^crm_data/$', gunshotViews.CrmData.as_view()),
    url(r'^gunshots/$', gunshotViews.GunshotList.as_view()),
    url(r'^gunshots/(?P<pk>[0-9]+)/$', gunshotViews.GunshotDetail.as_view()),
    url(r'^gunshots_multiple/$', gunshotViews.GunshotMultipleList.as_view()),
    url(r'^gunshots_multiple/(?P<pk>[0-9]+)/$', gunshotViews.GunshotMultipleDetail.as_view()),
    url(r'^sales_report/$', salesReportViews.SalesReport.as_view()),
    url(r'^print_report/$', printReportViews.PrintReport.as_view()),
    url(r'^mail_report/$', mailReportViews.MailReport.as_view()),
    url(r'^funnel_report/$', funnelReportViews.FunnelReport.as_view()),

)


urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
)