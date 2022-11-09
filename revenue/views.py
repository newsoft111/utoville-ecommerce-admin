from django.shortcuts import render
from .models import *
from django.db.models import Q
from datetime import datetime
from dateutil.relativedelta import relativedelta

def revenue_list(request):
	start_date = datetime.now()-relativedelta(months=1)
	end_date = datetime.now()

	if request.GET.get("start_date"):
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")
		if request.GET.get("end_date"):
			end_date = request.GET.get("end_date")
		

	RevenueAdmin.objects.filter(date__range = [start_date, end_date])
	return render(request, 'revenue/revenue_list.html')