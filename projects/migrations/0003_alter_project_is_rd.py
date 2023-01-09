# Generated by Django 4.1.5 on 2023-01-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_client_project_code1_project_code2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_rd',
            field=models.CharField(choices=[('1', 'Not'), ('2', 'Research'), ('3', 'Development')], max_length=1, verbose_name='Is it research and development project ?'),
        ),
    ]
