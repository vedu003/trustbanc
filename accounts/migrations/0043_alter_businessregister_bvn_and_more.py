# Generated by Django 4.0.5 on 2022-07-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_alter_product_typeofuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessregister',
            name='BVN',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='businessregister',
            name='NIN',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='individualregister',
            name='BVN',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='individualregister',
            name='NIN',
            field=models.CharField(max_length=200),
        ),
    ]