# Generated by Django 2.1 on 2018-09-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='read_free',
            field=models.BooleanField(default=False),
        ),
    ]