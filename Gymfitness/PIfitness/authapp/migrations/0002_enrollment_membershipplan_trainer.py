# Generated by Django 5.0 on 2024-02-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=10)),
                ('Phonenumber', models.CharField(max_length=12)),
                ('DOB', models.DateField()),
                ('SelectMembershipPlan', models.CharField(max_length=180)),
                ('SelectTrainer', models.CharField(max_length=50)),
                ('Reference', models.CharField(max_length=25)),
                ('Address', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=150)),
                ('price', models.IntegerField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('phonenumber', models.CharField(max_length=25)),
                ('salary', models.IntegerField(max_length=25)),
            ],
        ),
    ]