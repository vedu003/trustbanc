# Generated by Django 4.0.5 on 2022-07-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_remove_orderplaced_ordered_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='ordered_date1',
            field=models.DateField(default=0.0004997501249375312),
            preserve_default=False,
        ),
    ]
