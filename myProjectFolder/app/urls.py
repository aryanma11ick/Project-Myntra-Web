from django.urls import path
from . import views #. means from this partocular folder look for "views" file

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.index, name= "home"),
]
