# Generated by Django 4.2.3 on 2023-08-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_coupon_required_amount_to_use_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='required_amount_to_use_coupon',
            field=models.PositiveBigIntegerField(),
        ),
    ]