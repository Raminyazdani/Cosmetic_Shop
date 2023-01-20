# Generated by Django 4.1.4 on 2023-01-20 10:37

import Core.fields.ForeignKeys.ParentForeignKey
import Core.fields.ForeignKeys.ProductForeignKey
import Core.fields.ForeignKeys.UserForeignKey
import Core.fields.ManyToManys.ProductManyToMany
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=Core.fields.ForeignKeys.UserForeignKey.UserForeignKey(blank=True, help_text='Author id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_author', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=Core.fields.ForeignKeys.ProductForeignKey.ProductForeignKey(blank=True, help_text='Product of this Comment record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='Products.product', verbose_name='Comment`s Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=Core.fields.ForeignKeys.ParentForeignKey.ParentForeignKey(blank=True, help_text='Parent of this Category record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childes', to='Products.category', verbose_name='Category`s Parent'),
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=Core.fields.ManyToManys.ProductManyToMany.ProductManyToMany(blank=True, db_index=True, help_text='Product of this Category record', related_name='categorys', through='Products.ProductCategory', to='Products.product', verbose_name='Category`s Product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='product',
            field=Core.fields.ManyToManys.ProductManyToMany.ProductManyToMany(blank=True, db_index=True, help_text='Product of this Brand record', related_name='brands', through='Products.ProductBrand', to='Products.product', verbose_name='Brand`s Product'),
        ),
    ]
