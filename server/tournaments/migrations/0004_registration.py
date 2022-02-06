# Generated by Django 4.0.1 on 2022-02-05 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_remove_tournaments_competitors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('cancelled_on', models.DateTimeField(blank=True)),
                ('status', models.CharField(choices=[('REGISTERED', 'REGISTERED'), ('INTERESTED', 'INTERESTED'), ('CANCELLED', 'CANCELLED')], max_length=20)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_competitiors', to='tournaments.tournaments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tournaments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
