# Generated by Django 4.2.6 on 2023-11-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_superadmin',
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
