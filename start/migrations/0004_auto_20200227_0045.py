# Generated by Django 3.0.2 on 2020-02-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10)),
                ('type_name', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
                ('cost', models.DecimalField(decimal_places=0, max_digits=5)),
                ('income_outcome', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]
