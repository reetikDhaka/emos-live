# Generated by Django 3.2.4 on 2021-07-08 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmpAccounts', '0016_empdata_apporovedstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empdata',
            old_name='apporovedStatus',
            new_name='apporoved_Status',
        ),
    ]
