from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView  # new
from .views import SignUpView

urlpatterns = [
    #path('', views.main, name='main'),
    path("accounts/signup", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]