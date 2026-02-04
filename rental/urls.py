from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-car/', views.add_car_view, name='add_car'),
    path('add-customer/', views.add_customer_view, name='add_customer'),
    path('available/', views.available_cars_view, name='available_cars'),
    path('rent/', views.rent_view, name='rent_car'),
    path('return/', views.return_view, name='return_car'),
    path('customers/', views.customer_view, name='customers'),
    path('process-return/<str:customer_name>/<int:car_id>/', views.process_return, name='process_return'),
]
