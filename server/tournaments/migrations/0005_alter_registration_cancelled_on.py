# Generated by Django 4.0.1 on 2022-02-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='cancelled_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
