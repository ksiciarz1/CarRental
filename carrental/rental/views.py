from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html.jinja')


def cars(request):
    cars = Car.objects.all()
    categories = list(cars.values_list('category', flat=True).distinc())
    cars2 = pd.DataFrame.from_records(cars.values())

    return render(request, 'cars.html.jinja', {'cars': cars, 'categories': categories, 'cars2': cars2.to_html(classes='table table-striped table-bordereds', index=False)})


def car(request, car_id):
    return render(request, 'car.html.jinja')
