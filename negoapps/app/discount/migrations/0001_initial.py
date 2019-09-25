# Generated by Django 2.2.5 on 2019-09-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=16)),
                ('condition', models.CharField(choices=[('0', 'Amount'), ('1', 'Percentage')], default='1', max_length=1)),
                ('value', models.DecimalField(decimal_places=2, max_digits=18)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('limit', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
