# Generated by Django 3.2.6 on 2021-08-13 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_user_id', models.CharField(max_length=30)),
                ('follow_user_username', models.CharField(max_length=100)),
                ('followed_user_id', models.CharField(max_length=30)),
                ('followed_user_username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=5, null=True)),
                ('interests', models.JSONField(blank=True, default=list, null=True)),
                ('profpic', models.ImageField(blank=True, null=True, upload_to='user/profilepic')),
                ('introduction', models.TextField(blank=True)),
                ('following', models.IntegerField(default=0)),
                ('follower', models.IntegerField(default=0)),
                ('concertnum', models.IntegerField(default=0)),
                ('concertpcp', models.JSONField(blank=True, default=list, null=True)),
                ('userkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('tguser_id', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userinfo')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
