# Generated by Django 2.1.3 on 2018-11-14 14:27

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=140)),
                ('height', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=5)),
                ('weight', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=5)),
                ('city', models.CharField(blank=True, default='', max_length=140)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]