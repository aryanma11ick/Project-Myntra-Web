from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:category_name>/', views.category_page, name='category_page'),
]
