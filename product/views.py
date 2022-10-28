from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json, re
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


@login_required(login_url="account:login")
def product_write(request):
	seo = {
		'title': "체험단 모집 - 콘디",
	}

	if request.method == 'POST':
		jsonData = json.loads(request.body)
		product_name = jsonData.get('product_name')
		area = jsonData.get('area')
		price = re.sub(r'[^0-9]', '', jsonData.get('price'))
		thumbnail = jsonData.get('thumbnail')
		content = jsonData.get('content')

		if product_name is None or product_name == '':
			result = {'result': '201', 'result_text': '제목을 입력해주세요.'}
			return JsonResponse(result)
		if area is None or area == '':
			result = {'result': '201', 'result_text': '지역을 선택해주세요.'}
			return JsonResponse(result)
		if price is None or price == '':
			result = {'result': '201', 'result_text': '가격을 입력해주세요.'}
			return JsonResponse(result)
		if thumbnail is None or thumbnail == '':
			result = {'result': '201', 'result_text': '대표 이미지을 등록해주세요.'}
			return JsonResponse(result)
		if content is None or content == '':
			result = {'result': '201', 'result_text': '내용을 입력해주세요.'}
			return JsonResponse(result)

		
		try:
			product_obj = Product()
			product_obj.user = request.user
			product_obj.product_name = product_name
			product_obj.area = area
			product_obj.price = price
			product_obj.content = content
			product_obj.save()

			result = {'result': '200', 'result_text': '등록이 완료되었습니다.'}
			return JsonResponse(result)

		except Exception as e:
			print(e)
			result = {'result': '201', 'result_text': '알수없는 오류입니다. 관리자에게 문의해주세요.'}
			return JsonResponse(result)

	else:
		return render(request, 'product/product_write.html')


@login_required(login_url="account:login")
def product_upload_content_image(request):
	image = request.FILES['image']
			
	try:
		product_image_obj = ProductImage()
		product_image_obj.image = image
		product_image_obj.user = request.user
		product_image_obj.save()

		return JsonResponse({
			'result': '200',
			'result_text': product_image_obj.image.url
		})

	except Exception as e:
		print(e)
		return JsonResponse({
			'result': '201',
			'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
		})


@login_required(login_url="account:login")
def product_upload_thumbnail(request):
	thumbnail = request.FILES['thumbnail']

	try:
		product_thumbnail_obj = ProductThumbnail()
		product_thumbnail_obj.thumbnail = thumbnail
		product_thumbnail_obj.user = request.user
		product_thumbnail_obj.save()

		return JsonResponse({
			'result': '200',
			'result_text': product_image_obj.image.url
		})

	except Exception as e:
		return JsonResponse({
			'result': '201',
			'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
		})

