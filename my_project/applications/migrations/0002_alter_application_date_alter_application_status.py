# Generated by Django 4.0.4 on 2022-07-07 03:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 3, 1, 57, 147770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('On Review', 'On Review'), ('Selected', 'Selected'), ('Waiting Listed', 'Waiting Listed'), ('Rejected', 'Rejected')], default='Submitted', max_length=100),
        ),
    ]