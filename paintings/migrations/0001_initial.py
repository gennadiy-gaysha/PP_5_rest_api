# Generated by Django 3.2 on 2024-03-05 19:49

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
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('year_created', models.DateField()),
                ('technique', models.CharField(choices=[('Oil Paint', 'Oil Paint'), ('Acrylic Paint', 'Acrylic Paint'), ('Watercolor', 'Watercolor'), ('Gouache', 'Gouache'), ('Pastel', 'Pastel'), ('Charcoal', 'Charcoal'), ('Graphite', 'Graphite'), ('Ink', 'Ink'), ('Mixed Media', 'Mixed Media')], max_length=25)),
                ('theme', models.CharField(choices=[('Portrait', 'Portrait'), ('Still Life', 'Still Life'), ('Landscape', 'Landscape'), ('Seascape', 'Seascape'), ('Abstract', 'Abstract'), ('Figurative', 'Figurative'), ('Genre', 'Genre'), ('Animal', 'Animal')], max_length=25)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.CharField(choices=[('In stock', 'In stock'), ('Reserved', 'Reserved'), ('Sold', 'Sold')], max_length=25)),
                ('image', models.ImageField(blank=True, default='../default_painting_czwroy', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]