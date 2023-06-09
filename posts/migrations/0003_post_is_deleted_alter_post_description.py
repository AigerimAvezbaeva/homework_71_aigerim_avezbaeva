# Generated by Django 4.1.7 on 2023-04-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_post_created_at_post_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
    ]
