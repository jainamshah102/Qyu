# Generated by Django 3.1.7 on 2021-03-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationdetail',
            name='gstno',
            field=models.CharField(default='', max_length=15),
        ),
    ]
