<<<<<<< Updated upstream
# Generated by Django 4.1.4 on 2023-01-11 04:20
=======
# Generated by Django 4.1.4 on 2023-01-10 05:02
>>>>>>> Stashed changes

import Core.fields.ForeignKeys
import Core.fields.ManyToMany
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< Updated upstream
        ('Products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
>>>>>>> Stashed changes
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=Core.fields.ForeignKeys.CustomUserFieldForeignKey(help_text='Author id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_author', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=Core.fields.ForeignKeys.CustomProductFieldForeignKey(blank=True, help_text='Product of this Comment record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='Products.product', verbose_name='Comment`s Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
<<<<<<< Updated upstream
            field=Core.fields.ForeignKeys.CustomCategoryParentFieldForeignKey(blank=True, default=None, help_text='Parent of this Category record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='Products.category', verbose_name='Category`s Parent'),
=======
            field=Core.fields.ForeignKeys.CustomCategoryParentFieldForeignKey(blank=True, help_text='Parent of this Category record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_parent', to='Products.category', verbose_name='Category`s Parent'),
>>>>>>> Stashed changes
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=Core.fields.ManyToMany.CustomProductFieldManyToMany(blank=True, db_index=True, help_text='Product of this Category record', related_name='category_product', through='Products.ProductCategory', to='Products.product', verbose_name='Category`s Product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='product',
            field=Core.fields.ManyToMany.CustomProductFieldManyToMany(blank=True, db_index=True, help_text='Product of this Brand record', related_name='brand_product', through='Products.ProductBrand', to='Products.product', verbose_name='Brand`s Product'),
        ),
    ]
