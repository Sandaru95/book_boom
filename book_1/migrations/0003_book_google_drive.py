# Generated by Django 2.1.3 on 2018-11-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_1', '0002_book_read_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='google_drive',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
