# Generated by Django 4.1.4 on 2023-01-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Department',
            field=models.CharField(choices=[('General', 'General'), ('CS', 'CS'), ('IT', 'IT'), ('IS', 'IS'), ('AI', 'AI'), ('DS', 'DS')], max_length=7, null=True),
        ),
    ]