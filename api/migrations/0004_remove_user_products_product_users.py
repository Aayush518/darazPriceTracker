# Generated by Django 4.1.5 on 2023-01-31 11:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
