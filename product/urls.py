from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
	path('', views.product_list, name='list'),
	path('write/', views.product_write, name='write'),
	path('<int:product_id>/', views.product_update, name='update'),
	path('delete/', views.product_delete, name='delete'),
	path('upload/image', views.product_upload_content_image, name='upload_image'),
]