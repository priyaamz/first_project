# Generated by Django 4.0.1 on 2022-02-14 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='esla',
            new_name='esal',
        ),
    ]
