from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json, re

def profit_list(request):
	profit_objs = Profit.objects.all()
	profit_amount = profit_objs.aggregate(Sum('profit_amount'))['profit_amount__sum']
	if profit_amount is None:
		profit_amount = 0
	profit_done_objs = ProfitDone.objects.all()

	return render(request, 'profit/profit_list.html', {
		"profit_objs": profit_objs,
		'profit_amount': profit_amount,
		'profit_done_objs': profit_done_objs
	})