from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='shortner_home'),
    path('<str:url>', views.url_redirect, name='url_redirect')
]