# Generated by Django 3.1.7 on 2021-08-29 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleeka', '0019_auto_20210829_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savinggroup',
            old_name='groupName',
            new_name='name',
        ),
    ]