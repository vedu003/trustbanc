# Generated by Django 4.0.5 on 2022-07-10 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_alter_aboutinfosection_about_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutinfosection',
            old_name='box1_description',
            new_name='about_description2',
        ),
        migrations.RenameField(
            model_name='aboutinfosection',
            old_name='box2_description',
            new_name='about_description3',
        ),
    ]
