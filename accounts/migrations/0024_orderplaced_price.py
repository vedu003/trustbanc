# Generated by Django 4.0.5 on 2022-07-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_orderplaced_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='price',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]