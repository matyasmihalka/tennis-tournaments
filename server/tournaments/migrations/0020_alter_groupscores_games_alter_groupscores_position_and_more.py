# Generated by Django 4.0.1 on 2022-02-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0019_alter_eliminationdrawmatch_draw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupscores',
            name='games',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='groupscores',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='groupscores',
            name='sets_won',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
