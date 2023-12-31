# Generated by Django 4.2.1 on 2023-06-23 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FuelOrder',
            fields=[
                ('order_no', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('brief_description', models.CharField(max_length=255)),
                ('order_status', models.CharField(default='Pending', max_length=255)),
                ('date_created', models.DateField()),
                ('date', models.DateField(default=None)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FuelStation',
            fields=[
                ('station_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('fuel_capacity', models.IntegerField()),
                ('location_address', models.CharField(max_length=255)),
                ('fuel_units_received', models.FloatField()),
                ('fuel_units_supplied', models.FloatField()),
                ('fuel_units_left', models.FloatField()),
                ('total_fuel_cost', models.FloatField()),
                ('officer_in_charge', models.CharField(max_length=255)),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FuelSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('petrol_supplied', models.FloatField()),
                ('diesel_supplied', models.FloatField()),
                ('petrol_cost', models.FloatField()),
                ('diesel_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=250)),
                ('ref_no', models.CharField(max_length=255)),
                ('rations_a', models.CharField(max_length=255)),
                ('rations_b', models.CharField(max_length=255)),
                ('litres_petrol', models.FloatField()),
                ('litres_oil', models.FloatField()),
                ('Vehicle_number', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_no', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('vehicle_type', models.CharField(default=None, max_length=255)),
                ('current_mileage', models.IntegerField(null=True)),
                ('description', models.CharField(default=None, max_length=255)),
                ('distance_covered_kms', models.IntegerField()),
                ('fuel_consumed_litres', models.IntegerField()),
                ('fuel_cost', models.FloatField(null=True)),
                ('total_repairs', models.IntegerField()),
                ('repair_cost', models.FloatField(null=True)),
                ('total_cost', models.FloatField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WebApp.department')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('public_service_no', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile_number', models.IntegerField()),
                ('dob', models.DateField()),
                ('date_of_hire', models.DateField()),
                ('location_address', models.CharField(max_length=255)),
                ('email_address', models.CharField(default=None, max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WebApp.department')),
            ],
        ),
        migrations.CreateModel(
            name='StationsFuelRefill',
            fields=[
                ('station_refill_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('fuel_received', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('total_fuel_cost', models.FloatField()),
                ('date_received', models.DateField()),
                ('date_posted', models.DateField()),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.fuelstation')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.fuelsupply')),
            ],
        ),
        migrations.CreateModel(
            name='RepairAndMaintenance',
            fields=[
                ('repair_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('repair_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=255)),
                ('total_cost', models.IntegerField()),
                ('date_posted', models.DateField()),
                ('time', models.DateTimeField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.user')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('notification_id', models.IntegerField(primary_key=True, serialize=False)),
                ('notification_type', models.CharField(max_length=255)),
                ('notification_message', models.CharField(max_length=255)),
                ('is_read', models.BooleanField(default=False)),
                ('notification_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='FuelRefill',
            fields=[
                ('vehicle_refill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fuel_dispensed_ltrs', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('date_received', models.DateField()),
                ('Time', models.DateTimeField()),
                ('order_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.fuelorder')),
                ('served_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.user')),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.fuelstation')),
            ],
        ),
        migrations.AddField(
            model_name='fuelorder',
            name='approved_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.user'),
        ),
        migrations.AddField(
            model_name='fuelorder',
            name='driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_refill_orders_driver', to='WebApp.user'),
        ),
        migrations.AddField(
            model_name='fuelorder',
            name='vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_refill_orders_vehicle', to='WebApp.vehicle'),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.user')),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.vehicle')),
            ],
        ),
    ]
