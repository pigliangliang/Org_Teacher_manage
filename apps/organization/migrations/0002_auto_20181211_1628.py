# Generated by Django 2.0 on 2018-12-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=20, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=86, verbose_name='学习人数'),
        ),
    ]
