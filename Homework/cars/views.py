from django.shortcuts import render
from .models import Car


def viewCars(request):

    all = Car.objects.all()

    return render(request, 'list_orders.html', {'all': all})


def addCar(request):
    carBrand = request.POST.get("car_brand",False)
    carModel = request.POST.get("car_model",False)
    carHP = request.POST.get("car_hp",False)

    object = Car(brand=carBrand, model=carModel, hp=carHP)
    object.save()

    return render(request, 'car_order.html')

