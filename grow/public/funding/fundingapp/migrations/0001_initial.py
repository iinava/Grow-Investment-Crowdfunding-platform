# Generated by Django 3.2.18 on 2023-11-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30, unique=True)),
                ('role', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
