# Generated by Django 2.1.3 on 2018-12-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/images/a.jpeg', upload_to='static/images/'),
        ),
    ]
