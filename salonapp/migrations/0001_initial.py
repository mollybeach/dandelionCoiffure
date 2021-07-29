

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('appointmentdate', models.CharField(max_length=20)),
            ],
        ),
    ]

