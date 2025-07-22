
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('drumkits/', views.drumkits, name='drumkits'),

    path('plugins/', views.plugins, name='plugins'),

    path('samples/', views.samples, name='samples'),
    path('contact/', views.contact, name = 'contact'),
    path('listen/', views.listen, name = 'listen'),
]
