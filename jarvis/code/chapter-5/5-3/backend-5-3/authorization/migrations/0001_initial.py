# Generated by Django 2.0 on 2019-01-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_id', models.CharField(max_length=64, unique=True)),
                ('nickname', models.CharField(db_index=True, max_length=256)),
                ('focus_cities', models.TextField(default='[]')),
                ('focus_constellations', models.TextField(default='[]')),
                ('focus_stocks', models.TextField(default='[]')),
            ],
        ),
    ]
