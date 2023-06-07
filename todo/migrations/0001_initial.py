# Generated by Django 4.2.2 on 2023-06-07 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('Status', models.CharField(choices=[('OP', 'OPEN'), ('WO', 'WORKING'), ('DO', 'DONE'), ('OV', 'OVERDUE')], default='OP', max_length=2)),
                ('Due_date', models.DateField(blank=True, null=True)),
                ('Tags', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]