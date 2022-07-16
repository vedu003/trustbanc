# Generated by Django 4.0.5 on 2022-07-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_product_subproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessregister',
            name='company_email',
        ),
        migrations.AlterField(
            model_name='product',
            name='typeofuser',
            field=models.CharField(choices=[('business', 'business'), ('individual', 'individual')], max_length=200),
        ),
    ]
