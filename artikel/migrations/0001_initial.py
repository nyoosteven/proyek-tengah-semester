<<<<<<< Updated upstream
# Generated by Django 4.1 on 2022-10-27 20:23
=======
# Generated by Django 4.1 on 2022-10-27 18:59
>>>>>>> Stashed changes

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
            ],
        ),
    ]
