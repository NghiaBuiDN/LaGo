# Generated by Django 4.2.2 on 2023-06-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('phone', models.CharField(max_length=250, unique=True)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
    ]
