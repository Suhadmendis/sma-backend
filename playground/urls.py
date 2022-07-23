from django.urls import path
from . import views

urlpatterns = [
    path('verify/', views.verify),
    path('user/', views.getUser),

    path('operation1/', views.operation1),
    path('operation2/', views.operation2),
    path('operation3/', views.operation3),
    path('operation4/', views.operation4),
    path('operation5/', views.operation5),
    path('operation6/', views.operation6),
    path('operation7/', views.operation7),
    path('operation8/', views.operation8),
    path('operation9/', views.operation9),
    path('operation10/', views.operation10),
    path('operation11/', views.operation11),
    path('operation12/', views.operation12),
    path('operation13/', views.operation13),
]
