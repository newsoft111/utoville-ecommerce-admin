from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
	path('', views.product_list, name='list'),
	path('regist/', views.product_regist, name='regist'),
]