# Generated by Django 4.2.16 on 2024-11-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0005_alter_coworking_image_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coworking',
            name='image',
            field=models.ImageField(upload_to='image/coworking'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='image/project'),
        ),
    ]