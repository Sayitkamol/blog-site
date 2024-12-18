# Generated by Django 4.2 on 2024-12-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.FileField(upload_to='post-images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
