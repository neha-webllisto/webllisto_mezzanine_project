# Generated by Django 2.1.4 on 2019-01-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
