from django.urls import path
from .views import *

urlpatterns = [
    path('', index),       # приобращении к http://127.0.0.1:8000/
    path('test/', test),    # приобращении к http://127.0.0.1:8000/test/
]