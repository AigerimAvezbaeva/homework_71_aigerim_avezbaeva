# Generated by Django 4.1.7 on 2023-04-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_account_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='login',
            field=models.CharField(max_length=150, unique=True, verbose_name='Логин'),
        ),
    ]
