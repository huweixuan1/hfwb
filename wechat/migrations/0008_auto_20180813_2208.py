# Generated by Django 2.0.5 on 2018-08-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0007_auto_20180813_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_trade',
            name='area',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='house_trade',
            name='housetype',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='house_trade',
            name='img',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='house_trade',
            name='position',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='house_trade',
            name='price',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='house_trade',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='house', to='wechat.HouseTag'),
        ),
        migrations.AlterField(
            model_name='house_trade',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
