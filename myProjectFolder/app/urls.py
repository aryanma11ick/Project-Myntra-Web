from django.urls import path
from . import views #. means from this partocular folder look for "views" file


urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]