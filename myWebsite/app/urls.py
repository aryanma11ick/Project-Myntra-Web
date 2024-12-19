from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:category_name>/', views.category_page, name='category_page'),
    path('product/<str:category_name>/<int:product_id>/', views.product_page, name='product_page'),
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
