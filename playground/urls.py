from django.urls import path
from . import views

urlpatterns = [
    path('verify/', views.verify),
    path('user/', views.getUser),

    path('operation1/', views.getOperation1),
    path('operation2/', views.getOperation2),
    path('operation3/', views.getOperation3),
    path('operation4/', views.getOperation4),
    path('operation5/', views.getOperation5),
    path('operation6/', views.getOperation6),
    path('operation7/', views.getOperation7),
    path('operation8/', views.getOperation8),
    path('operation9/', views.getOperation9),
    path('operation10/', views.getOperation10),
    path('operation11/', views.getOperation11),
    path('operation12/', views.getOperation12),
    path('operation13/', views.getOperation13),
]
