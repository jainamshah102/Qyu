# Generated by Django 3.1.6 on 2021-03-01 11:11

from django.db import migrations, models
import django.db.models.deletion


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
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('max_participants', models.IntegerField()),
                ('avg_waiting_time', models.FloatField()),
                ('status', models.CharField(choices=[('R', 'registration'), ('A', 'active'), ('D', 'archive')], max_length=1)),
                ('security_key', models.CharField(blank=True, max_length=10, unique=True)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organizationdetail')),
            ],
        ),
    ]