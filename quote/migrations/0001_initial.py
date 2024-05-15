# Generated by Django 5.0.6 on 2024-05-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('quote', models.TextField()),
                ('retrieval_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
