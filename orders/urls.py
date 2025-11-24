
from django.urls import path
from . import views


urlpatterns = [
    path('place_order/',views.place_order,name='place_order'),
    # FOR PAYMENT PAGE 
    path('payments/',views.payments,name='payments'),
   
   
]
