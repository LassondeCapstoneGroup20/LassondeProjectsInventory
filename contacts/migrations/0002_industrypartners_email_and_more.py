# Generated by Django 4.1.6 on 2023-02-09 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrypartners',
            name='email',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='industrypartners',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]