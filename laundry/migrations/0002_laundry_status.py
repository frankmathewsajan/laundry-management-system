# Generated by Django 5.1.1 on 2024-09-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laundry',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
