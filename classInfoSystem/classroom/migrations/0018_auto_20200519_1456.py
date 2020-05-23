# Generated by Django 3.0.6 on 2020-05-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0006_remove_lecture_classroom_name'),
        ('classroom', '0017_auto_20200519_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='dep_name',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='l_name',
        ),
        migrations.AddField(
            model_name='classroom',
            name='lecture_name',
            field=models.ManyToManyField(to='lecture.Lecture', verbose_name='lecture name'),
        ),
    ]
