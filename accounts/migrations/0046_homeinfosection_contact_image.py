# Generated by Django 4.0.5 on 2022-07-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_remove_homeinfosection_contact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinfosection',
            name='contact_image',
            field=models.ImageField(default='img/123.png', upload_to='home/homeinfosection'),
        ),
    ]