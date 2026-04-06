from django.urls import path

from . import views

urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('registration_page', views.registration, name ='registration_page'),
]