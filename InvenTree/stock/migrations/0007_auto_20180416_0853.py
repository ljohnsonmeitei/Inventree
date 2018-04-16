# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0006_auto_20180415_1011'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0006_auto_20180415_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItemTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name='historicalstockitem',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalstockitem',
            name='location',
        ),
        migrations.RemoveField(
            model_name='historicalstockitem',
            name='part',
        ),
        migrations.RemoveField(
            model_name='historicalstockitem',
            name='stocktake_user',
        ),
        migrations.RemoveField(
            model_name='historicalstockitem',
            name='supplier_part',
        ),
        migrations.AddField(
            model_name='stockitem',
            name='batch',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_parts', to='stock.StockItem'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stockitems', to='supplier.Customer'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='serial',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='HistoricalStockItem',
        ),
        migrations.AddField(
            model_name='stockitemtracking',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_info', to='stock.StockItem'),
        ),
        migrations.AddField(
            model_name='stockitemtracking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
