from django.conf.urls import patterns, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from reports import views

urlpatterns = patterns('',
    url(r'^authentication/$', views.Authentication.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^$', views.Dashboard.as_view()),
    url(r'^logout/$', views.Logout.as_view()),
    url(r'^transactions/$', views.Transactions.as_view()),
    url(r'^create_lead/$', views.CreateLead.as_view()),
    url(r'^dashboard/$', views.Dashboard.as_view()),
    url(r'^reports/$', views.ReportList.as_view()),
    url(r'^reports/(?P<pk>[0-9]+)/$', views.ReportDetail.as_view()),
    url(r'^crm_data/$', views.CrmData.as_view()),
    url(r'^gunshots/$', views.GunshotList.as_view()),
    url(r'^gunshots/(?P<pk>[0-9]+)/$', views.GunshotDetail.as_view()),
    url(r'^gunshots_multiple/$', views.GunshotMultipleList.as_view()),
    url(r'^gunshots_multiple/(?P<pk>[0-9]+)/$', views.GunshotMultipleDetail.as_view()),
    url(r'^sales_report/$', views.SalesReport.as_view()),
    url(r'^print_report/$', views.PrintReport.as_view()),
    url(r'^mail_report/$', views.MailReport.as_view()),
    url(r'^funnel_report/$', views.FunnelReport.as_view()),

)


urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
)