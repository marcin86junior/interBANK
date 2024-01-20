# Generated by Django 3.2 on 2024-01-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_no',
            field=models.PositiveIntegerField(default=34, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawl')], max_length=10),
        ),
    ]
