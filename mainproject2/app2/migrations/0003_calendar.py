# Generated by Django 3.2.14 on 2022-08-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.IntegerField()),
                ('Occation', models.CharField(max_length=500)),
            ],
        ),
    ]