# Generated by Django 4.0.5 on 2022-06-30 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_businessregister_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('phone', models.PositiveIntegerField()),
                ('house_number', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
                ('NIN', models.PositiveIntegerField()),
                ('BVN', models.PositiveIntegerField()),
                ('joint_account', models.BooleanField(default=False)),
                ('signature', models.ImageField(upload_to='individualsignpic')),
                ('photo', models.ImageField(upload_to='individualprofilepic')),
                ('kin_name', models.CharField(max_length=200)),
                ('kin_relationship', models.CharField(max_length=200)),
                ('kin_phone', models.PositiveIntegerField()),
                ('kin_house_number', models.CharField(max_length=200)),
                ('kin_street_name', models.CharField(max_length=500)),
                ('kin_city', models.CharField(max_length=200)),
                ('kin_state', models.CharField(max_length=200)),
                ('kin_country', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnotherJoinAccountRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('another_name', models.CharField(max_length=200)),
                ('another_phone', models.PositiveIntegerField()),
                ('another_house_number', models.CharField(max_length=200)),
                ('another_street_name', models.CharField(max_length=500)),
                ('another_city', models.CharField(max_length=200)),
                ('another_state', models.CharField(max_length=200)),
                ('another_country', models.CharField(max_length=200)),
                ('another_birthdate', models.DateField()),
                ('another_gender', models.CharField(max_length=200)),
                ('another_occupation', models.CharField(max_length=200)),
                ('another_signature', models.ImageField(upload_to='anotherjointsignpic')),
                ('another_photo', models.ImageField(upload_to='anotherjointprofilepic')),
                ('kin_name', models.CharField(max_length=200)),
                ('kin_relationship', models.CharField(max_length=200)),
                ('kin_phone', models.PositiveIntegerField()),
                ('kin_house_number', models.CharField(max_length=200)),
                ('kin_street_name', models.CharField(max_length=500)),
                ('kin_city', models.CharField(max_length=200)),
                ('kin_state', models.CharField(max_length=200)),
                ('kin_country', models.CharField(max_length=200)),
                ('individual_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.individualregister')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]