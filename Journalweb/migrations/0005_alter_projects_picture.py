# Generated by Django 3.2.8 on 2022-05-21 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journalweb', '0004_auto_20220520_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Picture',
            field=models.ImageField(upload_to='Media'),
        ),
    ]
