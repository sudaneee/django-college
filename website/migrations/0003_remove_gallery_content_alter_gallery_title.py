# Generated by Django 4.1 on 2022-08-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='content',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
