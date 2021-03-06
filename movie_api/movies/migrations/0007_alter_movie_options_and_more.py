# Generated by Django 4.0.4 on 2022-04-30 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directors', '0001_initial'),
        ('movies', '0006_alter_movie_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movieType',
            new_name='movie_type',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='openingYear',
            new_name='opening_year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='director_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='directors.director'),
        ),
    ]
