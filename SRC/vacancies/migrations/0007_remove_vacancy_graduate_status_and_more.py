# Generated by Django 4.0.4 on 2022-04-16 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_vacancy_about_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='graduate_status',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='working_status',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='works_status',
        ),
    ]
