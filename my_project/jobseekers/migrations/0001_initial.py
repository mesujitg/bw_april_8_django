# Generated by Django 4.0.4 on 2022-06-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('qualification', models.TextField()),
                ('experience', models.TextField()),
                ('training', models.TextField()),
                ('skills', models.TextField()),
                ('cv', models.FileField(upload_to='cvs')),
                ('image', models.ImageField(upload_to='users')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
