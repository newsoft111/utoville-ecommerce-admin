from django.urls import path
from . import views

app_name = 'profit'

urlpatterns = [
	path('', views.profit_list, name='list'),

]