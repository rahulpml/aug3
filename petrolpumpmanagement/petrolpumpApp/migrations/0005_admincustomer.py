# Generated by Django 4.0.6 on 2022-07-29 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petrolpumpApp', '0004_item_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='admincustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuelquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='petrolpumpApp.customer')),
                ('fueltype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='petrolpumpApp.fueltype')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='petrolpumpApp.supplier')),
                ('tanker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='petrolpumpApp.tanker')),
            ],
        ),
    ]
