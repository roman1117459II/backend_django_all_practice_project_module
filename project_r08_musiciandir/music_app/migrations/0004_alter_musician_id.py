# Generated by Django 4.2.7 on 2024-01-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_alter_musician_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
