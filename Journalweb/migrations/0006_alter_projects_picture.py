# Generated by Django 3.2.8 on 2022-05-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journalweb', '0005_alter_projects_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Picture',
            field=models.ImageField(blank=True, null=True, upload_to='Media'),
        ),
    ]
