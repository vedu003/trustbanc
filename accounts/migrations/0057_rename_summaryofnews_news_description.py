# Generated by Django 4.0.5 on 2022-07-16 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='summaryofnews',
            new_name='description',
        ),
    ]
