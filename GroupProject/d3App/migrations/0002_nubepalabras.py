# Generated by Django 2.1.4 on 2018-12-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d3App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NubePalabras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('repeats', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-repeats',),
            },
        ),
    ]
