# Generated by Django 4.2.10 on 2024-02-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0003_module_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='number',
            field=models.IntegerField(),
        ),
    ]
