# Generated by Django 3.1.5 on 2021-02-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_usweb', '0003_auto_20210131_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_cd',
            field=models.DecimalField(decimal_places=0, max_digits=6, primary_key=True, serialize=False, verbose_name='社員番号'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification3',
            field=models.CharField(max_length=20, null=True),
        ),
    ]