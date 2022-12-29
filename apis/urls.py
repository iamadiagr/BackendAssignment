from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_api, name='get_api'),
    path('videos/', views.VideoListView.as_view(), name='Videos'),
]