from django.contrib import admin
from django.http import request
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from src import views

urlpatterns = [
    path("", views.index),
    path('contact', views.contact),
    path('about', views.about),
    path('upload', views.upload_file),
    path('sendFeedback',views.sendFeedback)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
