from django.shortcuts import render, redirect
from django.contrib import messages
from .logic import rental_system, Car, Customer
from .forms import CarForm, CustomerForm, RentForm
import random

def home(request):
    return render(request, 'rental/home.html')

def add_car_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car_id = random.randint(1000, 9999)
            new_car = Car(
                car_id, 
                form.cleaned_data['brand'], 
                form.cleaned_data['model'], 
                form.cleaned_data['year']
            )
            rental_system.add_car(new_car)
            messages.success(request, f"Car {new_car} added successfully!")
            return redirect('available_cars')
    else:
        form = CarForm()
    return render(request, 'rental/add_car.html', {'form': form})

def add_customer_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = Customer(form.cleaned_data['name'])
            rental_system.add_customer(new_customer)
            messages.success(request, f"Customer {new_customer.name} registered!")
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'rental/add_customer.html', {'form': form})

def available_cars_view(request):
    available = [car for car in rental_system.cars if car.available]
    return render(request, 'rental/available.html', {'cars': available})

def rent_view(request):
    available_cars = [car for car in rental_system.cars if car.available]
    if request.method == 'POST':
        form = RentForm(rental_system.customers, available_cars, request.POST)
        if form.is_valid():
            success = rental_system.rent_car(
                form.cleaned_data['customer'], 
                form.cleaned_data['car']
            )
            if success:
                messages.success(request, "Car rented successfully!")
            else:
                messages.error(request, "Failed to rent car.")
            return redirect('customers')
    else:
        form = RentForm(rental_system.customers, available_cars)
    return render(request, 'rental/rent.html', {'form': form, 'can_rent': len(available_cars) > 0 and len(rental_system.customers) > 0})

def return_view(request):
    customers_with_cars = [c for c in rental_system.customers if c.rented_cars]
    return render(request, 'rental/return.html', {'customers': customers_with_cars})

def process_return(request, customer_name, car_id):
    if rental_system.return_car(customer_name, car_id):
        messages.success(request, "Car returned successfully!")
    else:
        messages.error(request, "Error returning car.")
    return redirect('return_car')

def customer_view(request):
    return render(request, 'rental/customer.html', {'customers': rental_system.customers})
