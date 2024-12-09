# Generated by Django 4.2 on 2024-12-07 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('msm', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post_app.post')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='post_app.comment')),
            ],
        ),
    ]
