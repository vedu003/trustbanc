# Generated by Django 4.0.5 on 2022-06-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_number', models.PositiveIntegerField()),
                ('tax_id', models.PositiveIntegerField()),
                ('company_industry', models.CharField(max_length=200)),
                ('company_date', models.DateField()),
                ('company_email', models.EmailField(max_length=50)),
                ('NIN', models.PositiveIntegerField()),
                ('BVN', models.PositiveIntegerField()),
                ('phoneno', models.PositiveIntegerField()),
                ('houseno', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('em1', models.CharField(max_length=200)),
                ('em2', models.CharField(max_length=200)),
                ('em3', models.CharField(max_length=200)),
                ('em4', models.CharField(max_length=200)),
                ('signature', models.ImageField(upload_to='businesssignpic')),
                ('photo', models.ImageField(upload_to='businessprofilepic')),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
