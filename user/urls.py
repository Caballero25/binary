from django.urls import path
from . import views

urlpatterns = [
    path('users/login', views.userLogin, name="userLogin"),
    path('logout/', views.logout_view, name='logout'),
    path('', views.menu, name="menu-principal")
]