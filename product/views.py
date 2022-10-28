from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
import json
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
<<<<<<< Updated upstream
	
=======


@login_required(login_url="account:login")
def product_write(request):
	seo = {
		'title': "체험단 모집 - 콘디",
	}

	if request.method == 'POST':
		print(request.body)
		jsonData = json.loads(request.body)
		test = jsonData.get('qna_id')
		campaign_type = request.POST.get("campaign_type")
		category = request.POST.get("category")
		thumbnail = request.FILES['campaign_img']
		subject = request.POST.get("subject")
		provide = request.POST.get("provide")
		guide_line = request.POST.get("guide_line")
		keyword = request.POST.get("keyword")
		product_url = request.POST.get("product_url")
		channel = ",".join(request.POST.getlist("channel[]"))
		limit_offer = request.POST.get("limit_offer")
		finished_at = 7
		item = request.POST.get("item")
		company_address = request.POST.get("company_address")
		company_name = request.POST.get("company_name")
		if request.user.plan_at > datetime.now():
			reward = 0
		else:
			reward = re.sub(r'[^0-9]', '', request.POST.get('reward'))
		

		item_price = 0
		if item != 'default':
			item_price = item_price+10000
			if item == 'recommend':
				item_price = item_price+20000
				
		
		#pay_amount = (int(finished_at)-3)*2000+(int(limit_offer)*5000)+(int(reward)*int(limit_offer))+int(item_price)+100
		pay_amount = (int(limit_offer)*5000)+(int(reward)*int(limit_offer))+int(item_price)+100
		
		try:
			campaign = Campaign()
			campaign.campaign_type = campaign_type
			campaign.category = category
			campaign.subject = subject
			campaign.channel = channel
			campaign.thumbnail = thumbnail
			campaign.provide = provide
			campaign.guide_line = guide_line
			campaign.keyword = keyword
			if product_url is not None:
				campaign.product_url = product_url
			campaign.limit_offer = limit_offer
			if company_address is not None:
				campaign.company_address = company_address
			if request.user.plan_type != 0 and request.user.plan_at > datetime.now():
				campaign.is_paid = True
				campaign.pay_amount = 0
			else:
				campaign.pay_amount = pay_amount
			campaign.finished_at = datetime.now() + timedelta(days=int(finished_at))
			campaign.reward = reward
			campaign.user = request.user
			campaign.merchant_uid = None
			campaign.company_name = company_name
		

			if request.user.plan_type != 0 and request.user.plan_at > datetime.now():
				if not request.user.is_superuser:
					if request.user.plan_type == 1:
						campaign.is_item = True
					elif request.user.plan_type == 2:
						campaign.is_item = True
						campaign.is_recommend = True
				else:
					campaign.is_item = True
					campaign.is_recommend = True
			else:
				if item != 'default':
					campaign.is_item = True
					if item == 'recommend':
						campaign.is_recommend = True
			campaign.save()

			campaign = Campaign.objects.get(pk=campaign.pk)
			campaign.merchant_uid = str(datetime.now().strftime('%Y%m%d')) + str(campaign.pk) + str(random.randint(10000,99999))
			campaign.save()

			if request.user.is_superuser:
				shipping_address = UserShippingAddress.objects.get(pk=1)

				for i in range(random.randrange(50)):
					campaign_offer = CampaignOffer()
					campaign_offer.campaign = campaign
					campaign_offer.user = request.user
					campaign_offer.shipping_address = shipping_address
					campaign_offer.appeal = 'appeal'
					campaign_offer.sns_url = 'sns_url'
					campaign_offer.save()
					
			if request.user.plan_type != 0 and request.user.plan_at > datetime.now():
				result = '200'
				result_text = "등록이 완료되었습니다."
				next_url = resolve_url('UserCampaign')
			else:
				result = '200'
				result_text = "등록이 완료되었습니다.<br>결제창으로 이동합니다."
				next_url = resolve_url('CampaignPay', campaign.pk)
		except Exception as e:
			result = '201'
			result_text = '알수없는 오류입니다. 다시시도 해주세요.'
			next_url = ''

		result = {'result': result, 'result_text': result_text, "next_url":next_url}
		return JsonResponse(result)
	else:
		return render(request, 'product/product_write.html')


@login_required(login_url="account:login")
def campaign_upload_image(request):
	if request.method == 'POST':
		image = request.FILES['image']
				
		try:
			campaign_image = CampaignImage()
			campaign_image.image = image
			campaign_image.user = request.user
			campaign_image.save()

			result = '200'
			result_text = campaign_image.image.url
		except Exception as e:
			print(e)
			result = '201'
			result_text = '알수없는 오류입니다. 다시시도 해주세요.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)
	else:
		return redirect("Index")
>>>>>>> Stashed changes
