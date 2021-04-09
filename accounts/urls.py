from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/register/', views.register, name="register"),
    path('', views.index, name="home")
  
]