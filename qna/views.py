from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
import json
# Create your views here.

@login_required(login_url="account:login")
def qna_list(request):
	seo = {
		'title': "유토빌",
	}

	qna_objs =  QnA.objects.all().order_by('-id')
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(qna_objs, 12)
	qna_objs = pagenator.get_page(page)

	return render(request, 'qna/qna_list.html',{
		"seo": seo,
		"qna_objs": qna_objs,
	})


@login_required(login_url="account:login")
def qna_detail(request, qna_id):
	seo = {
		'title': "유토빌",
	}

	try:
		qna_obj = QnA.objects.get(pk=qna_id)
	except:
		return redirect('/')

	if request.method == 'POST':
		jsonData = json.loads(request.body)
		answer = jsonData.get('answer')
				
		try:
			qna_obj.answer = answer
			qna_obj.save()

			result = '200'
			result_text = "답변이 완료되었습니다."
		except:
			result = '201'
			result_text = '알수없는 오류입니다. 다시시도 해주세요.'

		return JsonResponse({
			'result': result, 
			'result_text': result_text
		})
	else:
		return render(request, 'qna/qna_detail.html',{
			"seo":seo,
			"qna_obj": qna_obj
		})


def qna_delete(request):
	seo = {
		'title': "유토빌",
	}
	jsonData = json.loads(request.body)
	qna_id = jsonData.get('qna_id')
	
	try:
		qna_obj = QnA.objects.get(pk=qna_id)
	except:
		return JsonResponse({
			'result': '201', 
			'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
		})

	try:
		qna_obj.is_delete = True
		qna_obj.deleted_at = datetime.now()
		qna_obj.save()

		result = '200'
		result_text = "거부가 완료되었습니다."
	except Exception as e:
		print(e)
		result = '201'
		result_text = '알수없는 오류입니다. 다시시도 해주세요.'

	return JsonResponse({
		'result': result, 
		'result_text': result_text
	})

	