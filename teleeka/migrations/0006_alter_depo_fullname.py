# Generated by Django 3.2.6 on 2021-08-27 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teleeka', '0005_depo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depo',
            name='fullname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teleeka.client'),
        ),
    ]
