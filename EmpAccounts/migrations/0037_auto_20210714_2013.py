# Generated by Django 3.2.4 on 2021-07-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpAccounts', '0036_oattendance_workingdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='oattendance',
            name='attendance',
            field=models.CharField(choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='workingdays',
            name='dates',
            field=models.DateField(unique=True),
        ),
    ]
