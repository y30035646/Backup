# Generated by Django 4.0.4 on 2022-05-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_en', '0010_remove_touchhistory_touchee'),
    ]

    operations = [
        migrations.AddField(
            model_name='touchhistory',
            name='touchee',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]