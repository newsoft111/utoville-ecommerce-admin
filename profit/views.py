from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json, re

def profit_list(request):
	return render(request, 'profit/profit_list.html')