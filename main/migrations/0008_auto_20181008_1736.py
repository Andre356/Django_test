# Generated by Django 2.1.2 on 2018-10-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181008_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='grupy',
        ),
        migrations.AddField(
            model_name='user',
            name='grupy',
            field=models.ManyToManyField(blank=True, null=True, related_name='group_set', to='main.Group'),
        ),
    ]
