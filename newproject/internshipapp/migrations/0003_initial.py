# Generated by Django 4.2.6 on 2023-10-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('internshipapp', '0002_delete_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
