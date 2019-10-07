# Generated by Django 2.2.4 on 2019-10-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=0)),
                ('personal_info_agreed', models.BooleanField(default=False)),
                ('text_agreed', models.BooleanField(default=False)),
                ('is_picked', models.BooleanField(default=False)),
            ],
        ),
    ]
