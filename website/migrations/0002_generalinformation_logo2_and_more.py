# Generated by Django 4.0.6 on 2022-08-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinformation',
            name='logo2',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='generalinformation',
            name='logo',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]