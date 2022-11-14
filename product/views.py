from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
import json, re
# Create your views here.

@login_required(login_url="account:login")
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
		product_name = request.POST.get('product_name')
		area = request.POST.get('area')
		price = re.sub(r'[^0-9]', '', request.POST.get('price'))
		content = request.POST.get('content')
		category_first = request.POST.get('category_first')
		category_second = request.POST.get('category_second')
		category_third = request.POST.get('category_third')
		options_data = request.POST.get('options_data')

		try:
			thumbnails = request.FILES.getlist('thumbnail')
		except:
			result = {'result': '201', 'result_text': '대표 이미지을 등록해주세요.'}
			return JsonResponse(result)

		if category_first is None or category_first == '':
			result = {'result': '201', 'result_text': '대분류를 선택해주세요.'}
			return JsonResponse(result)

		if category_second is None or category_second == '':
			result = {'result': '201', 'result_text': '중분류를 선택해주세요.'}
			return JsonResponse(result)
		
		try:
			category_third_obj = CategoryThird.objects.get(pk=category_third, parent__name=category_second)
		except:
			result = {'result': '201', 'result_text': '소분류를 선택해주세요.'}
			return JsonResponse(result)

		if product_name is None or product_name == '':
			result = {'result': '201', 'result_text': '제목을 입력해주세요.'}
			return JsonResponse(result)

		if area is None or area == '':
			result = {'result': '201', 'result_text': '지역을 선택해주세요.'}
			return JsonResponse(result)

		if price is None or price == '':
			result = {'result': '201', 'result_text': '가격을 입력해주세요.'}
			return JsonResponse(result)

		if content is None or content == '':
			result = {'result': '201', 'result_text': '내용을 입력해주세요.'}
			return JsonResponse(result)

		try:
			product_obj = Product()
			product_obj.user = request.user
			product_obj.category_first = category_third_obj.parent.parent
			product_obj.category_second = category_third_obj.parent
			product_obj.category_third = category_third_obj
			product_obj.product_name = product_name
			product_obj.price = price
			product_obj.content = content
			product_obj.save()

			for thumbnail in thumbnails:
				ProductThumbnail.objects.create(product=product_obj, thumbnail=thumbnail)

			if options_data:
				list_data = json.loads(options_data)
				for obj in list_data:
					for key, value in obj.items():
						prod_var_obj = ProductVariant.objects.create(product=product_obj, variant=key)
						for k, v in value.items():
							ProductVariantValue.objects.create(variant=prod_var_obj, value=k, price=v)

			result = {'result': '200', 'result_text': '등록이 완료되었습니다.'}
			return JsonResponse(result)

		except Exception as e:
			print(e)
			result = {'result': '201', 'result_text': '알수없는 오류입니다. 관리자에게 문의해주세요.'}
			return JsonResponse(result)

	else:
		l1_l2_l3_cat_data = {}
		l1_data = CategoryFirst.objects.all()
		for l1 in l1_data:
			if l1.name not in l1_l2_l3_cat_data:
				l1_l2_l3_cat_data[l1.name] = []
			l2_cats = CategorySecond.objects.filter(parent_id=l1.id)
			for l2_cat in l2_cats:
				l2_data = {}
				if l2_cat.name not in l2_data:
					l2_data[l2_cat.name] = []
				l3_cats = CategoryThird.objects.filter(parent_id=l2_cat.id)
				for l3_cat in l3_cats:
					l2_data[l2_cat.name].append({"name":l3_cat.name, "id":l3_cat.pk})
				l1_l2_l3_cat_data[l1.name].append(l2_data)
		return render(request, 'product/product_write.html', context={"cats_data": l1_l2_l3_cat_data})


@login_required(login_url="account:login")
def product_update(request, product_id):
	seo = {
		'title': "체험단 모집 - 콘디",
	}

	if request.method == 'POST':
		product_name = request.POST.get('product_name')
		area = request.POST.get('area')
		price = re.sub(r'[^0-9]', '', request.POST.get('price'))
		content = request.POST.get('content')
		category_first = request.POST.get('category_first')
		category_second = request.POST.get('category_second')
		category_third = request.POST.get('category_third')
		options_data = request.POST.get('options_data')

		try:
			thumbnails = request.FILES.getlist('thumbnail')
		except:
			result = {'result': '201', 'result_text': '대표 이미지을 등록해주세요.'}
			return JsonResponse(result)

		if category_first is None or category_first == '':
			result = {'result': '201', 'result_text': '대분류를 선택해주세요.'}
			return JsonResponse(result)

		if category_second is None or category_second == '':
			result = {'result': '201', 'result_text': '중분류를 선택해주세요.'}
			return JsonResponse(result)
		
		try:
			category_third_obj = CategoryThird.objects.get(pk=category_third, parent__name=category_second)
		except:
			result = {'result': '201', 'result_text': '소분류를 선택해주세요.'}
			return JsonResponse(result)

		if product_name is None or product_name == '':
			result = {'result': '201', 'result_text': '제목을 입력해주세요.'}
			return JsonResponse(result)

		if area is None or area == '':
			result = {'result': '201', 'result_text': '지역을 선택해주세요.'}
			return JsonResponse(result)

		if price is None or price == '':
			result = {'result': '201', 'result_text': '가격을 입력해주세요.'}
			return JsonResponse(result)

		if content is None or content == '':
			result = {'result': '201', 'result_text': '내용을 입력해주세요.'}
			return JsonResponse(result)

		try:
			product_obj = Product()
			product_obj.user = request.user
			product_obj.category_first = category_third_obj.parent.parent
			product_obj.category_second = category_third_obj.parent
			product_obj.category_third = category_third_obj
			product_obj.product_name = product_name
			product_obj.price = price
			product_obj.content = content
			product_obj.save()

			for thumbnail in thumbnails:
				ProductThumbnail.objects.create(product=product_obj, thumbnail=thumbnail)

			result = {'result': '200', 'result_text': '등록이 완료되었습니다.'}
			return JsonResponse(result)

		except Exception as e:
			print(e)
			result = {'result': '201', 'result_text': '알수없는 오류입니다. 관리자에게 문의해주세요.'}
			return JsonResponse(result)

	else:
		l1_l2_l3_cat_data = {}
		l1_data = CategoryFirst.objects.all()
		for l1 in l1_data:
			if l1.name not in l1_l2_l3_cat_data:
				l1_l2_l3_cat_data[l1.name] = []
			l2_cats = CategorySecond.objects.filter(parent_id=l1.id)
			for l2_cat in l2_cats:
				l2_data = {}
				if l2_cat.name not in l2_data:
					l2_data[l2_cat.name] = []
				l3_cats = CategoryThird.objects.filter(parent_id=l2_cat.id)
				for l3_cat in l3_cats:
					l2_data[l2_cat.name].append({"name":l3_cat.name, "id":l3_cat.pk})
				l1_l2_l3_cat_data[l1.name].append(l2_data)
		
		product_obj = get_object_or_404(Product, pk=product_id)

		return render(request, 'product/product_write.html', context={"cats_data": l1_l2_l3_cat_data})



def product_delete(request):
	jsonData = json.loads(request.body)
	product_id = jsonData.get('cart_item_id_arr')

	Product.objects.filter(pk__in=product_id).update(
		is_deleted = True, 
		deleted_at = datetime.now()
	)
	
	result = '200'
	result_text = '삭제가 완료되었습니다.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)


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
