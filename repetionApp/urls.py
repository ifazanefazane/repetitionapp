from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index, name='index' ),
    path('index/',views.index2, name='index2'),
    path('accepter/',views.accepter, name='accepter'),
]
