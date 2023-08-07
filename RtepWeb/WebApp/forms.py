from django import forms
from .models import User
from django.forms import ModelForm
from .models import FuelRefill,FuelOrder,Vehicle,Order,FuelSupply
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'public_service_no',
            'first_name',
            'last_name',
            'mobile_number',
            'dob',
            'date_of_hire',
            'department',
            'location_address',
            'email_address',
            'position',
            'password',
            'gender',
            'role',
        ]
class FuelRefillForm(ModelForm):
    
    class Meta:
        model = FuelRefill
        fields = ['order_no', 'station_id', 'served_by', 'fuel_dispensed_ltrs', 'unit_price', 'total_cost', 'date_received', 'Time']

class FuelOrderForm(ModelForm):
    class Meta:
        model = FuelOrder
        fields = ['order_no','driver_id','vehicle_id','brief_description','order_status','date_created','date','is_complete','approved_by']

class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_no', 'manufacturer', 'model', 'vehicle_type', 'current_mileage', 'description', 'department']

class CustomUserCreationForm(UserCreationForm):
     class Meta:
        model = User
        fields = [
            'public_service_no',
            'first_name',
            'last_name',
            'mobile_number',
            'dob',
            'date_of_hire',
            'department',
            'location_address',
            'email_address',
            'position',
            'password',
            'gender',
            'role',
        ]

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['profile_picture','first_name', 'last_name', 'email_address','mobile_number','department',
                  'position','password']


class DetailOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['to','ref_no','rations_a','rations_b','litres_petrol',
                  'litres_oil','Vehicle_number','date']
    labels = {
        'to': 'To',
        'ref_no': 'Ref. My L.P.O No.',
        'rations_a': 'A Rations',
        'rations_b': 'B Rations',
        'litres_petrol': 'Litres Petrol',
        'litres_oil': 'Litres Oil',
        'Vehicle_number': 'Vehicle Number Plate',
        'date': 'Date',
    }  

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['public_service_no', 'first_name', 'last_name',
                  'mobile_number', 'dob', 'date_of_hire', 'department', 
                  'location_address', 'email_address', 'position', 'password', 'gender', 'role']
        
        def save(self, commit=True):
            User = super(UserRegistrationForm,self).save(commit=False)
            User.set_password(self.cleaned_data['password'])
            if commit:
                User.save()
            return User
        
class FuelSupplyForm(forms.ModelForm):
    class Meta:
        model = FuelSupply 
        fields = ['vendor_name','petrol_supplied','diesel_supplied','petrol_cost','diesel_cost']
        labels = {'vendor_name': 'Vendor Name',
                  'petrol_supplied': 'Petrol Supplied(Litres)',
                  'diesel_supplied': 'diesel_supplied(Litres)',
                  'petrol_cost': 'Cost of Petrol',
                  'diesel_cost': 'Cost of Diesel',
                  }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__' 
