# Generated by Django 2.0 on 2019-01-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0013_auto_20181225_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test_label',
            field=models.CharField(default='', max_length=128),
        ),
    ]