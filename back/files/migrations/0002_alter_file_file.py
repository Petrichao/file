# Generated by Django 5.0.1 on 2024-02-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploaded_files'),
        ),
    ]
