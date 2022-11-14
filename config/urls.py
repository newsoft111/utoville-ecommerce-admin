from django.contrib import admin
from django.urls import path, include       #new
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
	path('', include('main.urls')),
	path('account/', include('account.urls')),
	path('order/', include('order.urls')),
	path('product/', include('product.urls')),
	path('qna/', include('qna.urls')),
	path('profit/', include('profit.urls')),
	path('revenue/', include('revenue.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)