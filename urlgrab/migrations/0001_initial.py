# Generated by Django 4.0.6 on 2022-07-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLGrab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shorted_url', models.URLField(default='http://127.0.0.8:8000/shorter')),
                ('direction_url', models.URLField(max_length=5000)),
                ('stored_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
