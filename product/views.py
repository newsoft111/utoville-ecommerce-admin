from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url="acount:login")
def product_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}
	product_list =  Product.objects.all().order_by( "-id")
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(product_list, 12)
	product_list = pagenator.get_page(page)

	return render(request, 'product/product_list.html',{
		"seo":seo,
		'product_list': product_list
	})

def product_write(request):
	return render(request, 'product/product_write.html')
	