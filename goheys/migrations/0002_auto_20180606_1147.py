# Generated by Django 2.0.6 on 2018-06-06 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goheys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_add',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='date_add',
            new_name='date_added',
        ),
    ]