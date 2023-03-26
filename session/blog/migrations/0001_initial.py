# Generated by Django 4.1.7 on 2023-03-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduce', models.TextField()),
                ('Email', models.EmailField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='blog_img')),
            ],
        ),
    ]
