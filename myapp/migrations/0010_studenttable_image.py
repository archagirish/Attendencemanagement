# Generated by Django 5.1.3 on 2025-02-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_attendancetable_studentid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttable',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
