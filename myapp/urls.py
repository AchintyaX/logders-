from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'), 
    path('about', views.about, name='about'),
    path('policy', views.policy, name='policy'),
    path('refer_earn', views.refer_earn, name='refer_earn'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'), 
]