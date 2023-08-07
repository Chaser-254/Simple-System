from django import views
from django.urls import path

from .views import home,vehicle_create,fuel_refill_view,fuel_supply_view, fuel_order_view,register,fuel,order_detail,login_view,profile,reset_password

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('fuel-refill/', fuel_refill_view, name='fuel-refill'),
    path('fuel-order/', fuel_order_view, name='fuel-order'),
    path('fuel/', fuel, name='fuel'),
    path('vehicle/create/', vehicle_create, name='vehicle_create'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('reset-password/', reset_password, name='reset_password'),
    path('order/',order_detail, name='order_detail'),
    path('fuel_supply/',fuel_supply_view,name='fuel_supply'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
