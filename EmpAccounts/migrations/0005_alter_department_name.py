# Generated by Django 3.2.4 on 2021-07-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpAccounts', '0004_auto_20210707_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default='java', max_length=50, null=True),
        ),
    ]
