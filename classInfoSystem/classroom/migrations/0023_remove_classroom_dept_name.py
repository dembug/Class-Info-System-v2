# Generated by Django 3.0.6 on 2020-05-19 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0022_auto_20200520_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='dept_name',
        ),
    ]
