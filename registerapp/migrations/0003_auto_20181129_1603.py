# Generated by Django 2.0 on 2018-11-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0002_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='answer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='request',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
