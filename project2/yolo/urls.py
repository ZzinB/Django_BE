# myapp/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
