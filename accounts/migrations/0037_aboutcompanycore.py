# Generated by Django 4.0.5 on 2022-07-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_abouttestinomials'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompanyCore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('core_image', models.ImageField(upload_to='home/companycore')),
            ],
        ),
    ]
