# Generated by Django 2.0.5 on 2018-08-20 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0013_auto_20180813_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
