# Generated by Django 2.1.2 on 2018-10-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_group_userzy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='userzy',
        ),
        migrations.AddField(
            model_name='user',
            name='grupy',
            field=models.ManyToManyField(to='main.Group'),
        ),
    ]
