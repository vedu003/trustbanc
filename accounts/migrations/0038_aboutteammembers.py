# Generated by Django 4.0.5 on 2022-07-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_aboutcompanycore'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('member_image', models.ImageField(upload_to='home/teammembers')),
            ],
        ),
    ]
