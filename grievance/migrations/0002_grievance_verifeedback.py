# Generated by Django 2.1.5 on 2019-02-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='verifeedback',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
