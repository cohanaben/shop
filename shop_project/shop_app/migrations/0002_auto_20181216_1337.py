# Generated by Django 2.1.3 on 2018-12-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/images/1.jpeg', upload_to='static/images/shoes/'),
        ),
    ]
