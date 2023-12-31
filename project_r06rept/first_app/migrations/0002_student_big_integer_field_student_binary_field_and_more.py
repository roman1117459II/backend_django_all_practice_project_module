# Generated by Django 4.2.7 on 2023-12-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='big_integer_field',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='binary_field',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='boolean_field',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='date_field',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='date_time_field',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='decimal_field',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='duration_field',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email_field',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='float_field',
            field=models.FloatField(null=True),
        ),
    ]
