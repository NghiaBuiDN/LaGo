# Generated by Django 4.2.2 on 2023-07-18 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_added',
        ),
    ]