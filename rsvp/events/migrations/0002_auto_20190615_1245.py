# Generated by Django 2.2.2 on 2019-06-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='Nothing to say here'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
