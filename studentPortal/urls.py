from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='student-portal-home'),
    # path('login', views.login, name='login'),
]