# Generated by Django 3.0.6 on 2020-05-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_auto_20200419_2156'),
        ('classroom', '0023_remove_classroom_dept_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='departman_ismi',
            field=models.ManyToManyField(to='department.Department', verbose_name='department name'),
        ),
    ]
