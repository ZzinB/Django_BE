from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('detail/<int:post_id>',views.detail, name="detail"),
    path('create/',views.create, name="create"),

  # path 경로들
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)