# Generated by Django 4.1 on 2022-09-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replays', '0004_replaystage_replaystage_unique_stage_per_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replaystage',
            name='score',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]