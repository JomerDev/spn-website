# Generated by Django 2.0.4 on 2018-04-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180424_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servercommand',
            old_name='dt',
            new_name='dt_created',
        ),
        migrations.AddField(
            model_name='servercommand',
            name='dt_processed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
