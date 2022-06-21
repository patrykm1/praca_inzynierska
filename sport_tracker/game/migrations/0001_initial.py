# Generated by Django 4.0.4 on 2022-05-15 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SportGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nazwa aktywności')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(blank=True, max_length=10, null=True, verbose_name='Wynik')),
                ('match_status', models.CharField(max_length=25, verbose_name='Match status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Autor meczu')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='game.sportgame', verbose_name='Gra')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to=settings.AUTH_USER_MODEL, verbose_name='Przeciwnik')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_winner', to=settings.AUTH_USER_MODEL, verbose_name='Wygrany')),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25, verbose_name='Status')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='game.match', verbose_name='Mecz')),
            ],
        ),
    ]