# Generated by Django 2.2.7 on 2020-09-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodelivery', '0017_fooditems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order', to='foodelivery.OrderItem'),
        ),
    ]