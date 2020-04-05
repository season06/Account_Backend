# Generated by Django 3.0.2 on 2020-02-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('start', '0002_auto_20200225_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('money', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
