# Generated by Django 4.0.6 on 2022-08-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]