# Generated by Django 3.1.5 on 2021-01-31 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_usweb', '0002_auto_20210131_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='qualification1',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification2',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification3',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
