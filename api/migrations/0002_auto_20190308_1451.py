# Generated by Django 2.1.7 on 2019-03-08 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('short_name', models.TextField()),
                ('full_name', models.TextField()),
                ('type', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'ordering': ('institution', 'short_name'),
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institutions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.BankAccount')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='api.Institution'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]
