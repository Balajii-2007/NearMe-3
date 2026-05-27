from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('place/<str:slug>/', views.place_detail, name='place_detail'),
]
