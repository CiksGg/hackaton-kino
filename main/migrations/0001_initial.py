# Generated by Django 4.1.4 on 2022-12-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('year', models.IntegerField()),
                ('genre', models.CharField(choices=[('фантастика', 'fantasy'), ('боевик', 'thriller'), ('детектив', 'detective'), ('комедия', 'comedy'), ('мелодрама', 'melodrama'), ('научный', 'science'), ('приключения', 'adventures'), ('ужасы', 'horror'), ('спорт', 'sport'), ('мультфильм', 'cartoon'), ('документальный', 'documentary')], max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('actors', models.TextField()),
                ('duration', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='films')),
                ('video', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
