# Generated by Django 3.1.7 on 2021-03-25 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('W', 'waiting'), ('L', 'left'), ('R', 'removed'), ('C', 'complete')], default='W', max_length=1)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.userdetail')),
            ],
            options={
                'unique_together': {('user_id', 'event_id')},
            },
        ),
    ]
