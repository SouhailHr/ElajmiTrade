# Generated by Django 3.0.9 on 2021-09-26 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_tel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='tel',
            new_name='phone',
        ),
    ]