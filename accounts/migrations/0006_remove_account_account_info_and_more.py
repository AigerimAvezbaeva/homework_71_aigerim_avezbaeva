# Generated by Django 4.1.7 on 2023-04-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_phone_number_account_phone_account_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='account_info',
        ),
        migrations.RemoveField(
            model_name='account',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='account',
            name='user_info',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Информация о пользователе'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='account',
            name='login',
            field=models.CharField(default='inst_login', max_length=150, unique=True, verbose_name='Логин'),
        ),
    ]
