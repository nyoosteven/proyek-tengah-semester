
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cards_anxiety',
        ),
        migrations.DeleteModel(
            name='Cards_depression',
        ),
        migrations.DeleteModel(
            name='Cards_eating',
        ),
        migrations.DeleteModel(
            name='Cards_mood',
        ),
        migrations.DeleteModel(
            name='Cards_ptsd',
        ),
        migrations.DeleteModel(
            name='Cards_schizophrenia',
        ),
    ]