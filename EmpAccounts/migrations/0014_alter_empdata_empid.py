# Generated by Django 3.2.4 on 2021-07-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpAccounts', '0013_alter_empdata_empid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdata',
            name='empID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
