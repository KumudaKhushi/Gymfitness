# Generated by Django 5.0 on 2024-02-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_alter_membershipplan_price_alter_trainer_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(max_length=45),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.IntegerField(max_length=25),
        ),
    ]
