# Generated by Django 4.1.7 on 2023-03-09 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]