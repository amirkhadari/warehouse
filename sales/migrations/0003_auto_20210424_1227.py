# Generated by Django 3.1.5 on 2021-04-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210424_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]