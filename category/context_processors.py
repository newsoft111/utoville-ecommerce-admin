from .models import *
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
import json

def categories(request):
	data = {}
	category_first_obj = CategoryFirst.objects.all()
	for categoryFirst in category_first_obj:
		data[categoryFirst.name] = {}

		for categorySecond in categoryFirst.categorysecond_set.all():
			data[categoryFirst.name][categorySecond.name] = []
			
			for categoryThird in categorySecond.categorythird_set.all():
				data[categoryFirst.name][categorySecond.name].append(categoryThird.name)
			
	data = str(data)
	return {
		'categories': data
	}