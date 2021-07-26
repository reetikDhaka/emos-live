# Generated by Django 3.2.4 on 2021-07-07 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpAccounts', '0003_alter_empdata_empaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='empdata',
            name='Department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EmpAccounts.department'),
        ),
    ]
