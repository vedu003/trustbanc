# Generated by Django 4.0.5 on 2022-07-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_homebanner_homeexploreproducts_homeinfosection_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTestinomials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('testi_image', models.ImageField(upload_to='home/testinomials')),
            ],
        ),
    ]
