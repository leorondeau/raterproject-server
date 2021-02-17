# Generated by Django 3.1.6 on 2021-02-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamer',
            name='bio',
            field=models.CharField(default='new', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(),
        ),
    ]