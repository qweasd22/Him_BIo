# Generated by Django 5.1.2 on 2024-10-16 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appHim', '0006_rename_userformdata_userform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserForm',
            new_name='UserFormData',
        ),
    ]
