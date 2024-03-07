# Generated by Django 3.2 on 2024-03-07 19:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0002_auto_20240307_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='followed_id',
            new_name='followed',
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('owner', 'followed')},
        ),
    ]