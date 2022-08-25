from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='name_path_home'),       # приобращении к http://127.0.0.1:8000/
    path('seller/<int:seller_id>/', get_seller, name='name_path_seller'),
    path('catalog/<int:advert_id>/', view_advert, name='name_path_view_advert'),
    path('catalog/add-advert/', add_advert, name='name_path_add_advert'),
    # path('test/', test),    # приобращении к http://127.0.0.1:8000/test/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)