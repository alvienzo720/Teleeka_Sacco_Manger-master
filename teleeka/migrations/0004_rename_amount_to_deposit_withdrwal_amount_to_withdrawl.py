# Generated by Django 3.2.6 on 2021-08-26 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleeka', '0003_auto_20210826_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrwal',
            old_name='amount_to_deposit',
            new_name='amount_to_withdrawl',
        ),
    ]
