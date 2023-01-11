# Generated by Django 4.1.4 on 2023-01-10 05:31

import Core.fields.ForeignKeys
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=Core.fields.ForeignKeys.CustomCategoryParentFieldForeignKey(blank=True, default=None, help_text='Parent of this Category record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='Products.category', verbose_name='Category`s Parent'),
        ),
    ]