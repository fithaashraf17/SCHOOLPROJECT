# Generated by Django 4.0.1 on 2022-01-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=200)),
                ('lname', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('date', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=200)),
                ('exam', models.CharField(default='', max_length=200)),
                ('time', models.CharField(default='', max_length=200)),
                ('standard', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
            ],
        ),
    ]