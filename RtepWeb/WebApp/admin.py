from django.contrib import admin
from .models import User, Vehicle, Driver, RepairAndMaintenance, FuelSupply, FuelStation, StationsFuelRefill,Notifications,Department

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(RepairAndMaintenance)
admin.site.register(FuelSupply)
admin.site.register(FuelStation)
admin.site.register(StationsFuelRefill)
admin.site.register(Notifications)
admin.site.register(Department)
