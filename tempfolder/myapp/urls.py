from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_details),
]