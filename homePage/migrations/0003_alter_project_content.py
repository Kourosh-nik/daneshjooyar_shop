# Generated by Django 4.2.16 on 2024-11-25 08:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_alter_projectimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]