# Generated by Django 4.0.6 on 2022-07-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petrolpumpApp', '0008_remove_customer_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='profilepic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/')),
            ],
        ),
    ]
