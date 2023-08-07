from django.db import models         

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=255)

class User(models.Model):
    public_service_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.IntegerField()
    dob = models.DateField()
    date_of_hire = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    location_address = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, default=None)
    position = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

class Vehicle(models.Model):
    license_no = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255, default=None)
    current_mileage = models.IntegerField(null=True)
    description = models.CharField(max_length=255, default=None)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    distance_covered_kms = models.IntegerField()
    fuel_consumed_litres = models.IntegerField()
    fuel_cost = models.FloatField(null=True)
    total_repairs = models.IntegerField()
    repair_cost = models.FloatField(null=True)
    total_cost = models.FloatField(null=True)

class Driver(models.Model):
    driver = models.ForeignKey('User', on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

class RepairAndMaintenance(models.Model):
    repair_id = models.IntegerField(primary_key=True, auto_created=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    repair_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=255)
    total_cost = models.IntegerField()
    date_posted = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()

class FuelSupply(models.Model):
    vendor_name = models.CharField(max_length=255)
    petrol_supplied = models.FloatField()
    diesel_supplied = models.FloatField()
    petrol_cost = models.FloatField()
    diesel_cost = models.FloatField()

class FuelStation(models.Model):
    station_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    fuel_capacity = models.IntegerField()
    location_address = models.CharField(max_length=255)
    fuel_units_received = models.FloatField()
    fuel_units_supplied = models.FloatField()
    fuel_units_left = models.FloatField()
    total_fuel_cost = models.FloatField()
    officer_in_charge = models.CharField(max_length=255)
    contact_no = models.IntegerField()

class StationsFuelRefill(models.Model):
    station_refill_id = models.IntegerField(primary_key=True, auto_created=True)
    vendor_id = models.ForeignKey(FuelSupply, on_delete=models.CASCADE)
    station_id = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    fuel_received = models.FloatField()
    unit_price = models.FloatField()
    total_fuel_cost = models.FloatField()
    date_received = models.DateField()
    date_posted = models.DateField()
class FuelOrder(models.Model):
    order_no = models.IntegerField(primary_key=True, auto_created=True)
    driver_id = models.ForeignKey(User, related_name='fuel_refill_orders_driver', on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, related_name='fuel_refill_orders_vehicle', on_delete=models.CASCADE)
    brief_description = models.CharField(max_length=255,null=False)
    order_status = models.CharField(max_length=255, default="Pending")
    date_created = models.DateField()
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    is_complete = models.BooleanField(default=False)
    
class Notifications(models.Model):
    notification_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=255,null=False)
    notification_message = models.CharField( max_length=255, null=False)
    is_read = models.BooleanField(default=False)
    notification_date = models.DateTimeField()

class FuelRefill(models.Model):
    vehicle_refill_id = models.IntegerField(primary_key=True)
    order_no = models.ForeignKey(FuelOrder, on_delete=models.CASCADE)
    station_id = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    served_by = models.ForeignKey(User, on_delete=models.CASCADE)
    fuel_dispensed_ltrs = models.FloatField()
    unit_price = models.FloatField()
    total_cost = models.FloatField()
    date_received = models.DateField()
    Time = models.DateTimeField()

class Order(models.Model):
    to = models.CharField(max_length=250)
    ref_no = models.CharField(max_length=255)
    rations_a = models.CharField(max_length=255)
    rations_b = models.CharField(max_length=255)
    litres_petrol = models.FloatField()
    litres_oil = models.FloatField()
    Vehicle_number = models.CharField(max_length=255)
    date = models.DateField()