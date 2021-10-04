from django.urls import path
from. import views

urlpatterns = [

    path('', views.viewCars, name="viewCars"),
    path('addcar', views.addCar, name="addCar")
]