# Generated by Django 2.2.7 on 2019-11-17 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191116_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]