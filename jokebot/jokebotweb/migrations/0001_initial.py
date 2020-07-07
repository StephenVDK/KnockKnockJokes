# Generated by Django 3.0.8 on 2020-07-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jokeStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstPhrase', models.CharField(max_length=256)),
                ('secondPhrase', models.CharField(max_length=256)),
                ('jokeCount', models.IntegerField(default=0)),
            ],
        ),
    ]
