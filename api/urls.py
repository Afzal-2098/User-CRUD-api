from django.urls import path
from . import views

# API's urlpatterns
urlpatterns = [
    path('userapi/', views.UserApi.as_view(), name='userapi'),
    path('userapi/<int:pk>/', views.UserApi.as_view(), name='userapi'),
]