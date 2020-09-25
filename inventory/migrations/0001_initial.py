# Generated by Django 3.1.1 on 2020-09-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.ImageField(upload_to='')),
                ('status', models.CharField(default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.ImageField(upload_to='')),
                ('status', models.CharField(default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.ImageField(upload_to='')),
                ('status', models.CharField(default='Sold', max_length=10)),
                ('description', models.CharField(default='try', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]