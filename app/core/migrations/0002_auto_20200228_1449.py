# Generated by Django 3.0.3 on 2020-02-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
