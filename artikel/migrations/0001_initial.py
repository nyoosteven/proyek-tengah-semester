
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('tipe', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cards_anxiety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards_depression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards_eating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards_mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards_ptsd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cards_schizophrenia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
    ]
