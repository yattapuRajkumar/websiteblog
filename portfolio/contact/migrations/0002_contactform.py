# Generated by Django 4.0.3 on 2022-11-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
