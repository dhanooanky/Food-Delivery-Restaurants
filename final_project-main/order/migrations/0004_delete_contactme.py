# Generated by Django 3.2.8 on 2021-12-23 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_contactme_delete_contactus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contactme',
        ),
    ]