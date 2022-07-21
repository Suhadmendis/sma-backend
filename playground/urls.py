from django.urls import path
from . import views

urlpatterns =[
    path('verify/', views.verify),
    path('user/', views.getUser)
]