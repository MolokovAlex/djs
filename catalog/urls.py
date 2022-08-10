from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),       # приобращении к http://127.0.0.1:8000/
    # path('test/', test),    # приобращении к http://127.0.0.1:8000/test/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)