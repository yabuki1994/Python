# Generated by Django 3.1.5 on 2021-01-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_usweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='メール'),
        ),
    ]
