# Generated by Django 4.2.2 on 2023-06-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_a', models.CharField(max_length=255)),
                ('so_b', models.CharField(max_length=255)),
            ],
        ),
    ]
