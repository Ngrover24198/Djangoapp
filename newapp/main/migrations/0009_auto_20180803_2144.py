# Generated by Django 2.0.7 on 2018-08-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_blog_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]