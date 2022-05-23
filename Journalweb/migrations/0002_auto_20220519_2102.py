# Generated by Django 3.2.8 on 2022-05-20 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Journalweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_topic', models.CharField(max_length=50)),
                ('project_title', models.CharField(max_length=50)),
                ('submitted_by', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('project_file', models.FileField(upload_to='')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Journalweb.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]