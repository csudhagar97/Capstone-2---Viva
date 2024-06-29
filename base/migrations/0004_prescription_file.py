# Generated by Django 3.2.23 on 2024-04-30 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20240427_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='files/'),
            preserve_default=False,
        ),
    ]