# Generated by Django 3.1.7 on 2021-04-23 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField()),
                ('message', models.CharField(blank=True, default='', max_length=100)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organizationdetail')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.userdetail')),
            ],
            options={
                'unique_together': {('user_id', 'organization_id')},
            },
        ),
    ]
