# Generated by Django 4.0.5 on 2022-10-07 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Django3App', '0003_rename_regparent_regparentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regparentmodel',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='regparentmodel',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='regparentmodel',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.RenameField(
            model_name='regparentmodel',
            old_name='relation',
            new_name='relation1',
        ),
    ]