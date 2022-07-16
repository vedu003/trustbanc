# Generated by Django 4.0.5 on 2022-07-01 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_businessregister_checked_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='productpic')),
            ],
        ),
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('sub_title2', models.CharField(max_length=200)),
                ('product_detail_title', models.TextField()),
                ('benifits', models.TextField()),
                ('plan_feature', models.TextField()),
                ('sub_product_image', models.ImageField(upload_to='subproductpic')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.product')),
            ],
        ),
    ]