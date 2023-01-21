# Generated by Django 4.1.4 on 2023-01-20 17:55

import Core.fields.ForeignKeys.InventoryItemForeignKey
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Markets', '0002_inventory_date_close_inventory_date_open_and_more'),
        ('Customers', '0005_remove_ordercustomer_couponcustomercoupon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='inventory_item',
            field=Core.fields.ForeignKeys.InventoryItemForeignKey.InventoryItemForeignKey(blank=True, help_text='Cart of this Item record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartitems', to='Markets.inventoryitem', verbose_name='Item`s Cart'),
        ),
    ]
