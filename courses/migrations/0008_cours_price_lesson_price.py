# Generated by Django 4.2.5 on 2023-10-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='price',
            field=models.IntegerField(default=200, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.IntegerField(default=10, verbose_name='цена'),
        ),
    ]