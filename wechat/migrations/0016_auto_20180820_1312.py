# Generated by Django 2.0.5 on 2018-08-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0015_auto_20180820_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
