# Generated by Django 4.0.1 on 2022-01-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_remove_tournamnets_users_tournamnets_competitors'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamnets',
            name='name',
            field=models.CharField(default='CUP', max_length=100),
        ),
    ]
