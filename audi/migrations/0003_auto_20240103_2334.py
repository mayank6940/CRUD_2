# Generated by Django 3.2.23 on 2024-01-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audi', '0002_membership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='desc_text',
        ),
        migrations.AddField(
            model_name='membership',
            name='Gold_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='Platinium_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='Silver_text',
            field=models.TextField(null=True),
        ),
    ]