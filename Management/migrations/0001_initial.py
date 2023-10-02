# Generated by Django 4.1.7 on 2023-03-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmpId', models.IntegerField(primary_key=True, serialize=False)),
                ('EmpName', models.CharField(max_length=64)),
                ('Role', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Manager_ID', models.IntegerField()),
                ('Phone_No', models.CharField(max_length=10)),
                ('Email_ID', models.CharField(max_length=30)),
                ('IFSC_code', models.CharField(max_length=15)),
                ('Door_No', models.IntegerField()),
                ('Street', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=20)),
                ('Pin_code', models.IntegerField()),
                ('DOB', models.DateField()),
                ('DOJ', models.DateField()),
                ('PAN_No', models.CharField(max_length=10)),
                ('Acc_No', models.IntegerField()),
                ('Loan_taken', models.BooleanField()),
                ('Max_no_of_leaves', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=12)),
                ('EffectiveDate', models.DateField()),
                ('Grade', models.CharField(max_length=64)),
                ('Salary', models.FloatField()),
                ('PFTax', models.FloatField()),
                ('IncomeTax', models.FloatField()),
                ('BasicPay', models.FloatField()),
                ('HRA', models.FloatField()),
                ('Conveyance', models.FloatField()),
                ('Allowance', models.FloatField()),
            ],
        ),
    ]
