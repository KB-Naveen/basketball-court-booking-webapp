# Generated by Django 3.1.7 on 2021-03-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='academy',
            table='blog_member',
        ),
    ]
