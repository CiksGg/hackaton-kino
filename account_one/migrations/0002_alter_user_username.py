# Generated by Django 4.1.4 on 2022-12-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
