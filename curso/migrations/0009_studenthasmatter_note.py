# Generated by Django 2.2.1 on 2019-07-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0008_remove_studenthasmatter_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthasmatter',
            name='note',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
