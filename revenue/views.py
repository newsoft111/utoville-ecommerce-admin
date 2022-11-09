from django.shortcuts import render
from .models import *

# Create your views here.
def revenue_list(request):

	return render(request, 'revenue/revenue_list.html')