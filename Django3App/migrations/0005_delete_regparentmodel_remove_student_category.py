# Generated by Django 4.0.5 on 2022-11-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Django3App', '0004_rename_email_regparentmodel_email1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegParentModel',
        ),
        migrations.RemoveField(
            model_name='student',
            name='category',
        ),
    ]
