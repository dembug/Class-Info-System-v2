# Generated by Django 3.0.6 on 2020-05-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_auto_20200518_2300'),
        ('lecture', '0004_lecture_classroom_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='classroom_name',
            field=models.ManyToManyField(to='classroom.Classroom', verbose_name='Classroom Name'),
        ),
    ]
