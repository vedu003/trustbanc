# Generated by Django 4.0.5 on 2022-06-30 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_anotherjoinaccountregister_kin_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individualregister',
            old_name='photo',
            new_name='individual_photo',
        ),
        migrations.RenameField(
            model_name='individualregister',
            old_name='signature',
            new_name='individual_signature',
        ),
    ]
