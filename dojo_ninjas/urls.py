from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('processninja', views.processninja),
    path('processdojo', views.processdojo)
]
