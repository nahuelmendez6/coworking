# Generated by Django 5.1.4 on 2024-12-14 00:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TimeField(blank=True, null=True)),
                ('capacity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spaces', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='spaces.space')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userReview', to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='spaces.space')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='spaces.space')),
            ],
        ),
        migrations.CreateModel(
            name='SpaceAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('street_number', models.CharField(blank=True, max_length=10, null=True)),
                ('floor', models.CharField(blank=True, max_length=10, null=True)),
                ('apartment', models.CharField(blank=True, max_length=10, null=True)),
                ('reference', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='spaces.city')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='spaces.department')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province', to='spaces.department')),
            ],
        ),
        migrations.AddField(
            model_name='space',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='spaces.spaceaddress'),
        ),
        migrations.CreateModel(
            name='SpaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='spaces/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='spaces.space')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='spaces.day')),
                ('fromHour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromHour', to='spaces.hour')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workingHours', to='spaces.space')),
                ('untilHour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='untilHour', to='spaces.hour')),
            ],
        ),
    ]