# Generated by Django 2.1.7 on 2019-04-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('b', 'Borrowed')], default='a', max_length=1),
        ),
    ]
