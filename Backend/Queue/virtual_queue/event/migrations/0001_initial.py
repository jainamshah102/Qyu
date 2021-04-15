# Generated by Django 3.1.7 on 2021-03-25 05:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('start_date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end_date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('max_participants', models.IntegerField()),
                ('avg_waiting_time', models.FloatField()),
                ('status', models.CharField(choices=[('R', 'registration'), ('A', 'active'), ('D', 'archive')], max_length=1)),
                ('security_key', models.CharField(blank=True, default='', max_length=10, unique=True)),
                ('is_private', models.BooleanField(default=False)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organizationdetail')),
            ],
        ),
    ]
