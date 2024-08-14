# Generated by Django 4.2 on 2024-06-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pid', models.IntegerField()),
                ('Pname', models.CharField(max_length=20)),
                ('Pprice', models.FloatField()),
                ('Pimg', models.ImageField(upload_to='images/')),
                ('Pmfg', models.DateField()),
            ],
        ),
    ]
