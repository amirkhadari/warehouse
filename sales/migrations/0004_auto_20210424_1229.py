# Generated by Django 3.1.5 on 2021-04-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20210424_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
