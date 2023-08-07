from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import FuelRefillForm, FuelOrderForm, FuelSupplyForm
from django.contrib.auth.models import User
from .forms import UserProfileForm,DetailOrderForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VehicleForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        new_user = User.objects.create_user(username=email, email=email, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        public_service_no = request.POST['public_service_no']
        password = request.POST['password']
        user = authenticate(username=public_service_no, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Public Service No'})
    return render(request, 'login.html')

@login_required(login_url='login')
def fuel(request):
    return render(request, 'fuel.html')

@login_required(login_url='login')
def fuel_refill_view(request):
    form = FuelRefillForm()

    if request.method == 'POST':
        form = FuelRefillForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'fuel_refill_form.html', {'form': form})

@login_required(login_url='login')
def fuel_order_view(request):
    form = FuelOrderForm()

    if request.method == 'POST':
        form = FuelOrderForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'fuel_order.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    form = UserProfileForm(instance=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'profile.html', {'form': form})

UserModel = get_user_model()

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            public_service_number = form.cleaned_data['public_service_number']
            phone_number = form.cleaned_data['phone_number']
            
    
            try:
                user = UserModel.objects.get(public_service_number=public_service_number, phone_number=phone_number)
            except UserModel.DoesNotExist:
                return render(request, 'reset_password.html', {'form': form, 'error_message': 'Invalid public service number or phone number.'})
            
            token = default_token_generator.make_token(user)
            
            reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': user.id, 'token': token}))
            send_mail(
                'Password Reset',
                f'Please click the following link to reset your password: {reset_link}',
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )
            
            return render(request, 'reset_password.html', {'success_message': 'Password reset instructions have been sent to your email.'})
    else:
        form = PasswordResetForm()
    
    return render(request, 'reset_password.html', {'form': form})

def order_detail(request):
    if request.method == 'POST':
        form = DetailOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = DetailOrderForm()
    return render(request, 'order_detail.html',{'form': form})

def fuel_supply_view(request):
    if request.method == 'POST':
        form =FuelSupplyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FuelSupplyForm()
    return render(request,'fuel_supply.html', {'form': form})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

