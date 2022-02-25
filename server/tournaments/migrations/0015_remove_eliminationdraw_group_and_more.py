# Generated by Django 4.0.1 on 2022-02-24 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0014_alter_setstat_group_alter_setstat_tournament_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eliminationdraw',
            name='group',
        ),
        migrations.AddField(
            model_name='eliminationdraw',
            name='tournament',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournaments'),
            preserve_default=False,
        ),
    ]