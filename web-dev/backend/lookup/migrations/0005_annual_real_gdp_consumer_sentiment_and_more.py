# Generated by Django 4.0.3 on 2022-04-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0004_overview_alter_earning_surprise_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annual_Real_GDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumer_Sentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_10year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_2year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_30year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_3month_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_5year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_7year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily_Federal_Funds_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Durables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inflation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inflation_Expectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_10year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_2year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_30year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_3month_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_5year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_7year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_Cpi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_Federal_Funds_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Nonfarm_Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quarterly_Real_GDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Real_GDP_Per_Capita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Retail_Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Semiannual_Cpi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unemployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_10year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_2year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_30year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_3month_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_5year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_7year_Treasury_Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weekly_Federal_Funds_Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CPI',
        ),
    ]
