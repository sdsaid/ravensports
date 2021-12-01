# Generated by Django 3.2.9 on 2021-12-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamId', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('fullName', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('shortName', models.CharField(max_length=50)),
                ('allStar', models.BooleanField()),
                ('nbaFranchise', models.BooleanField()),
                ('league', models.CharField(max_length=50)),
                ('confName', models.CharField(max_length=50)),
                ('divName', models.CharField(max_length=50)),
            ],
        ),
    ]