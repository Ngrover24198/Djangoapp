# Generated by Django 2.0.7 on 2018-08-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180806_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
