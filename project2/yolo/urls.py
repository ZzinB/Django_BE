# myapp/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('detail/<int:post_id>',views.detail, name="detail"),
    path('detail/<int:post_id>/delete/',views.delete, name="delete"),
    path('create/',views.upload_image,  name="create"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
