# Generated by Django 4.0.5 on 2022-07-06 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_orderplaced_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.subproduct'),
        ),
    ]
