# Generated by Django 2.2.1 on 2019-05-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaNam', '0002_auto_20190504_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
