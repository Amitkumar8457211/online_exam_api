# Generated by Django 3.1.2 on 2020-11-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0002_auto_20201106_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertable',
            name='questionid',
            field=models.IntegerField(),
        ),
    ]