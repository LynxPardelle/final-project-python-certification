# Generated by Django 5.0.1 on 2024-01-29 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='descripción',
            new_name='description',
        ),
    ]
