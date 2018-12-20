# Generated by Django 2.1.4 on 2018-12-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d3App', '0002_nubepalabras'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('ratio', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('-ratio',),
            },
        ),
    ]
