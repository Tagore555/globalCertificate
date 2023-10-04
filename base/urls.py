from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('edit/<str:pk>/', views.edit, name="edit"), 
    path('check/',views.check,name="check"),
]
