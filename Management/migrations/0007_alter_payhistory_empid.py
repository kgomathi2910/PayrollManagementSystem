# Generated by Django 4.1.7 on 2023-03-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_payhistory_leave_unique_leave_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payhistory',
            name='EmpId',
            field=models.CharField(max_length=12),
        ),
    ]