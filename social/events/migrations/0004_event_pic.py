# Generated by Django 3.2.5 on 2023-06-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pic',
            field=models.ImageField(default='default.png', upload_to='path/to/event-img'),
        ),
    ]