from modules.funnelReport.models import GsFunnelDataMonthly,GsFunnelLabel
from modules.salesReport.models import GsReportFunnel,GsReportFunnelMultiple
from modules.vtigerCrm.models import VtigerGroups,VtigerLeaddetails,VtigerLeadaddress,VtigerCrmentity, VtigerUsers,VtigerLeadscf
from modules.funnelReport.serializers import GsFunnelDataMonthlySerializer,GsFunnelLabelSerializer
from modules.salesReport.serializers import GsReportFunnelSerializer,GsReportFunnelMultipleSerializer
from modules.vtigerCrm.serializers import VtigerGroupsSerializer,VtigerLeaddetailsSerializer,VtigerLeadaddressSerializer,VtigerCrmentitySerializer
from django.db.models import Q
from django.utils import timezone
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, pdfkit
from django.shortcuts import render,redirect
import datetime
from django.core.mail import EmailMessage
from django.db.models import Sum,Count
from django.db import connection
import crypt
import urllib2
import gunshot.settings as settings

class SalesReport(APIView):
    
    def get(self, request, format=None):
        if request.session.get('user_id', False) or (request.GET.get('print')=='true'):
            now = datetime.datetime.now()
            name="Aayush"
            #Truncations
            truncate_date_yearly = connection.ops.date_trunc_sql('year','created')
            truncate_date_monthly = connection.ops.date_trunc_sql('month','created')
            truncate_date_daily = connection.ops.date_trunc_sql('day','created')
            named_grouped_yearly= []
            named_grouped_monthly= []
            named_grouped_daily=[]

            gs_objects = GsReportFunnel.objects.all()[0:10]

            #All time data grouped by Assgn_First_Name
            data=GsReportFunnel.objects.exclude(assgn_last_name = "Group").values('assgn_first_name').annotate(sales=Sum('amount'))
            
            #Total Yearly Data
            gs = GsReportFunnel.objects.extra({'year':truncate_date_yearly})
            yearly = gs.values('year').annotate(Sum('amount'), Count('pk')).order_by('year')
       
            #Total Monthly Data
            gs = GsReportFunnel.objects.extra({'month':truncate_date_monthly})
            monthly = gs.values('month').annotate(Sum('amount'), Count('pk')).order_by('month')   

            #Total Daily Data
            gs = GsReportFunnel.objects.extra({'day':truncate_date_daily})
            daily = gs.values('day').annotate(Sum('amount'), Count('pk')).order_by('day')

            #Grouped Yearly,Monthly,Daily Data
            for d in data:
                grouped_obj = GsReportFunnel.objects.filter(assgn_first_name = d['assgn_first_name'])
                
                grouped_yearly= []
                gs_y= grouped_obj.extra({'year':truncate_date_yearly})
                yearly_grouped = gs_y.values('year').annotate(Sum('amount'), Count('pk')).order_by('year')
                grouped_yearly.append(yearly_grouped)
                named_grouped_yearly.append({'assgn_first_name':d['assgn_first_name'],'total_sales':d['sales'],'grouped_yearly':grouped_yearly})
                
                grouped_monthly= []
                gs_m= grouped_obj.extra({'month':truncate_date_monthly})
                monthly_grouped = gs_m.values('month').annotate(Sum('amount'), Count('pk')).order_by('month')
                grouped_monthly.append(monthly_grouped)
                named_grouped_monthly.append({'assgn_first_name':d['assgn_first_name'],'total_sales':d['sales'],'grouped_monthly':grouped_monthly})
                
                grouped_daily=[]
                gs_d= grouped_obj.extra({'day':truncate_date_daily})
                daily_grouped = gs_d.values('day').annotate(Sum('amount'), Count('pk')).order_by('day')
                grouped_daily.append(daily_grouped)
                named_grouped_daily.append({'assgn_first_name':d['assgn_first_name'],'total_sales':d['sales'],'grouped_daily':grouped_daily})
            
            # Get unique months, years, days for graphs
            unique_years= []
            for gy in named_grouped_yearly:
                for y in gy['grouped_yearly'][0]:
                    year = str(y['year'].year)
                    unique_years.append(year)
            unique_years= list(reversed(sorted(list(set(unique_years)))))
            
            unique_months= []
            for gm in named_grouped_monthly:
                for m in gm['grouped_monthly'][0]:
                    month = str(m['month'].month)+'/'+str(m['month'].year)
                    unique_months.append(month)
            unique_months= list(set(unique_months))
            unique_months=list(reversed(sorted(unique_months, key=lambda x: datetime.datetime.strptime(x, '%m/%Y'))))

            
            unique_days= []
            for gd in named_grouped_daily:
                for d in gd['grouped_daily'][0]:
                    day = str(d['day'].day)+'/'+str(d['day'].month)+'/'+str(d['day'].year)
                    unique_days.append(day)
            unique_days= list(set(unique_days))
            unique_days=list(reversed(sorted(unique_days, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))))
            
            final_yearly =[]
            for gy in named_grouped_yearly:
                yearly_data = []
                for uy in unique_years:
                    flag = False
                    for y in gy['grouped_yearly'][0]:
                        if str(y['year'].year) == uy:
                            yearly_data.append({"year": uy,"amount": y['amount__sum']})
                            flag = True
                    if flag == False :
                        yearly_data.append({"year": uy,"amount": "0"})
                fy = {'assgn_first_name':gy['assgn_first_name'], 'total_sales':gy['total_sales'], 'yearly_data': yearly_data}
                final_yearly.append(fy)    
            named_grouped_yearly = final_yearly

            final_monthly =[]
            for gm in named_grouped_monthly:
                monthly_data = []
                for um in unique_months:
                    flag = False
                    for m in gm['grouped_monthly'][0]:
                        if str(m['month'].month)+'/'+str(m['month'].year) == um:
                            monthly_data.append({"month": um,"amount": m['amount__sum']})
                            flag = True
                    if flag == False :
                        monthly_data.append({"month": um,"amount": "0"})
                fm = {'assgn_first_name':gm['assgn_first_name'], 'total_sales':gm['total_sales'], 'monthly_data': monthly_data}
                final_monthly.append(fm)    
            named_grouped_monthly = final_monthly

            final_daily =[]
            for gd in named_grouped_daily:
                daily_data = []
                for ud in unique_days:
                    flag = False
                    for d in gd['grouped_daily'][0]:
                        if str(d['day'].day)+'/'+str(d['day'].month)+'/'+str(d['day'].year) == ud:
                            daily_data.append({"day": ud,"amount": d['amount__sum']})
                            flag = True
                    if flag == False :
                        daily_data.append({"day": ud,"amount": "0"})
                fd = {'assgn_first_name':gd['assgn_first_name'], 'total_sales':gd['total_sales'], 'daily_data': daily_data}
                final_daily.append(fd)    
            named_grouped_daily = final_daily

            bar_series =[]
            for d in named_grouped_monthly[0:10]:
                temp_data=[]
                for um in unique_months[0:5]:
                    for m in d['monthly_data']:
                        if m['month'] == um:
                            temp_data.append(float(m['amount']))
                temp ={'name': d['assgn_first_name'].encode("utf-8"), 'data': temp_data }
                bar_series.append(temp)
            bar_categories= unique_months[0:5]

            pie_data=[]
            temp_total = 0
            for d in named_grouped_yearly[0:10]:
                temp_total += d['total_sales']

            for d in named_grouped_yearly[0:10]:
                temp = []
                temp.append(d['assgn_first_name'].encode("utf-8"))
                temp.append(float(d['total_sales'])/temp_total*100)
                pie_data.append(temp)

            monthly_max = {'month':str(max(monthly)['month'].month)+'/'+str(max(monthly)['month'].year),'amount': str(max(monthly)['amount__sum'])}
            return render(request, 'sales_report.html', {'root_url':settings.ROOT_URL,'monthly_max':monthly_max,'gs_objects': gs_objects,'pie_data': pie_data,'bar_categories': bar_categories,'bar_series':bar_series,'unique_years':unique_years,'unique_months':unique_months,'unique_days':unique_days,'current_date': now, 'name':name,'data':data,'monthly': monthly,'yearly': yearly,'daily': daily,'named_grouped_yearly':named_grouped_yearly,'named_grouped_monthly':named_grouped_monthly,'named_grouped_daily':named_grouped_daily})

        else:
            return redirect('/login')