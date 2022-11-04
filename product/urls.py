from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
	path('', views.product_list, name='list'),
	path('write/', views.product_write, name='write'),
	path('delete/', views.product_delete, name='delete'),
	path('l2_l3_category/', views.L2L3Category, name='l2_l3_category'),
	path('upload/image', views.product_upload_content_image, name='upload_image'),
]