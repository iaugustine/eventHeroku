# Generated by Django 3.0.3 on 2020-05-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addevent', '0011_events_e_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='e_sales',
            field=models.IntegerField(),
        ),
    ]
