# Generated by Django 3.1.4 on 2020-12-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]
