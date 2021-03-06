# Generated by Django 3.0.2 on 2020-02-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0004_auto_20200227_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10)),
                ('type_name', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=0, max_digits=5)),
                ('in_out_come', models.CharField(max_length=10)),
            ],
        )
    ]
