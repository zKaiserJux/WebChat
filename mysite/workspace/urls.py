from django.urls import path
from . import views

urlpatterns = [
     path("login/", views.render_login),
     path("admin/", views.login_admin),
     path('signup/', views.render_signup)
]