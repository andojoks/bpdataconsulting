# Generated by Django 5.1.6 on 2025-02-10 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_service_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='name',
        ),
    ]
