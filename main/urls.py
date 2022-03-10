from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('innovaciones/', views.innovaciones, name='innovaciones'),
    # path('contacto/', views.contacto, name='contacto'),
]