# Generated by Django 2.2 on 2020-10-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201101_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='content',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
