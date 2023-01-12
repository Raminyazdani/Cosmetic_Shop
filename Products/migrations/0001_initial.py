# Generated by Django 4.1.4 on 2023-01-11 19:28

import Core.ProjectMixins.Apps.Products_Mixins.ModelRequiredProperties
import Core.fields.BoleanFields
import Core.fields.CharFields
import Core.fields.DateFields
import Core.fields.DecimalFields
import Core.fields.ForeignKeys
import Core.fields.IdFields
import Core.fields.ManyToMany
import Core.fields.PositiveIntegerFields
import Core.fields.SlugFields
import Core.fields.TextFields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('name', Core.fields.CharFields.Name(db_index=True, help_text= 'Name of this Brand record', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message= 'must be a valid name with 3 to 30 characters', regex= '^.{3,30}$')], verbose_name= 'Brand`s Name')),
                ('slug', Core.fields.SlugFields.Slug(blank=True, help_text= 'Slug of this Brand record', max_length=100, null=True, unique=True, verbose_name= 'Brand`s Slug')),
                ('is_available', Core.fields.BoleanFields.IsAvailable(db_index=True, default=True, help_text= 'Is this Brand record available ?', verbose_name= 'Brand`s availability')),
                ('description', Core.fields.TextFields.Description(blank=True, help_text= 'description of this Brand record', max_length=1000, null=True, validators=[django.core.validators.MinLengthValidator(10, message= 'Description must be at least 10 characters'), django.core.validators.MaxLengthValidator(1000, message= 'Description must be at most 1000 characters')], verbose_name= 'Brand`s description')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
            bases=(Core.ProjectMixins.Apps.Products_Mixins.ModelRequiredProperties.BrandMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('name', Core.fields.CharFields.Name(db_index=True, help_text= 'Name of this Category record', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message= 'must be a valid name with 3 to 30 characters', regex= '^.{3,30}$')], verbose_name= 'Category`s Name')),
                ('slug', Core.fields.SlugFields.Slug(blank=True, help_text= 'Slug of this Category record', max_length=100, null=True, unique=True, verbose_name= 'Category`s Slug')),
                ('description', Core.fields.TextFields.Description(blank=True, help_text= 'description of this Category record', max_length=1000, null=True, validators=[django.core.validators.MinLengthValidator(10, message= 'Description must be at least 10 characters'), django.core.validators.MaxLengthValidator(1000, message= 'Description must be at most 1000 characters')], verbose_name= 'Category`s description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(Core.ProjectMixins.Apps.Products_Mixins.ModelRequiredProperties.CategoryMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('title', Core.fields.CharFields.Title(help_text= 'Title of this Comment record', max_length=20, validators=[django.core.validators.RegexValidator(message= 'Title must be a valid string with 3 to 20 characters', regex= '^.{3,20}$')], verbose_name= 'Comment`s Title')),
                ('body', Core.fields.TextFields.Body(help_text= 'Body of this Comment record', max_length=250, validators=[django.core.validators.MinLengthValidator(10, message= 'Body must be at least 10 characters'), django.core.validators.MaxLengthValidator(250, message= 'Body must be at most 250 characters')], verbose_name= 'Comment`s Body')),
                ('rating', Core.fields.PositiveIntegerFields.Rating(db_index=True, default=0, help_text= 'Rating of this Comment record', validators=[django.core.validators.MinValueValidator(0, message= 'Rating must be at least 0'), django.core.validators.MaxValueValidator(10, message= 'Rating must be at most 10')], verbose_name= 'Comment`s Rating')),
                ('is_active', Core.fields.BoleanFields.IsActive(db_index=True, default=True, help_text= 'Is this Comment record available ?', verbose_name= 'Comment`s availability')),
                ('slug', Core.fields.SlugFields.Slug(blank=True, help_text= 'Slug of this Comment record', max_length=100, null=True, unique=True, verbose_name= 'Comment`s Slug')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(Core.ProjectMixins.Apps.Products_Mixins.ModelRequiredProperties.CommentMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('name', Core.fields.CharFields.Name(db_index=True, help_text= 'Name of this Product record', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message= 'must be a valid name with 3 to 30 characters', regex= '^.{3,30}$')], verbose_name= 'Product`s Name')),
                ('slug', Core.fields.SlugFields.Slug(blank=True, help_text= 'Slug of this Product record', max_length=100, null=True, unique=True, verbose_name= 'Product`s Slug')),
                ('short_description', Core.fields.CharFields.ShortDescription(help_text= 'Short Description of this Product record', max_length=100, validators=[django.core.validators.MinLengthValidator(3, message= 'Short description must be at least 3 characters'), django.core.validators.MaxLengthValidator(100, message= 'Short description must be at most 100 characters')], verbose_name= 'Product`s Short Description')),
                ('description', Core.fields.TextFields.Description(blank=True, help_text= 'description of this Product record', max_length=1000, null=True, validators=[django.core.validators.MinLengthValidator(10, message= 'Description must be at least 10 characters'), django.core.validators.MaxLengthValidator(1000, message= 'Description must be at most 1000 characters')], verbose_name= 'Product`s description')),
                ('price', Core.fields.DecimalFields.PriceDollar(db_index=True, decimal_places=2, default=0.0, help_text= 'Dollar Price of this Product record', max_digits=10, validators=[django.core.validators.MinValueValidator(0, message= 'Price must be at least 0'), django.core.validators.MaxValueValidator(1000000000, message= 'Price must be at most 1000000000')], verbose_name= 'Product`s Dollar Price')),
                ('is_available', Core.fields.BoleanFields.IsAvailable(db_index=True, default=True, help_text= 'Is this Product record available ?', verbose_name= 'Product`s availability')),
                ('gender', Core.fields.PositiveIntegerFields.Gender(choices=[(0, 'Gender free'), (1, 'For men'), (2, 'For women')], db_index=True, default=0, help_text= 'UNISEX/MALE/FEMALE as integers', validators=[django.core.validators.MinValueValidator(0, message= 'Gender is integer ,must be at least 0'), django.core.validators.MaxValueValidator(2, message= 'Gender is integer ,must be at most 2')], verbose_name= 'Product`s Gender')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(Core.ProjectMixins.Apps.Products_Mixins.ModelRequiredProperties.ProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('product_id', Core.fields.ForeignKeys.ForeignKeyProduct(blank=True, help_text= 'Product of this Tag record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'producttags', to= 'Products.product', verbose_name= 'Tag`s Product')),
            ],
            options={
                'verbose_name': 'Product Tag',
                'verbose_name_plural': 'Products and Tags',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('name', Core.fields.CharFields.Name(db_index=True, help_text= 'Name of this Tag record', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message= 'must be a valid name with 3 to 30 characters', regex= '^.{3,30}$')], verbose_name= 'Tag`s Name')),
                ('slug', Core.fields.SlugFields.Slug(blank=True, help_text= 'Slug of this Tag record', max_length=100, null=True, unique=True, verbose_name= 'Tag`s Slug')),
                ('product', Core.fields.ManyToMany.ManyToManyProduct(blank=True, db_index=True, help_text= 'Product of this Tag record', related_name= 'tag_product', through= 'Products.ProductTag', to= 'Products.product', verbose_name= 'Tag`s Product')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
            bases=(Core.ProjectMixins.Apps.Products_Mixins.ModelRequiredProperties.TagMixin, models.Model),
        ),
        migrations.AddField(
            model_name='producttag',
            name='tag_id',
            field=Core.fields.ForeignKeys.ForeignKeyTag(blank=True, help_text= 'Product of this Tag record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'producttags', to= 'Products.tag', verbose_name= 'Tag`s Product'),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('category_id', Core.fields.ForeignKeys.ForeignKeyCategory(blank=True, help_text= 'Product of this Category record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'productcategorys', to= 'Products.category', verbose_name= 'Category`s Product')),
                ('product_id', Core.fields.ForeignKeys.ForeignKeyProduct(blank=True, help_text= 'Product of this Category record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'productcategorys', to= 'Products.product', verbose_name= 'Category`s Product')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Products and Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', Core.fields.IdFields.Id(db_index=True, help_text= 'Id of this Model record', primary_key=True, serialize=False, verbose_name= 'Model`s Id')),
                ('is_delete', Core.fields.BoleanFields.IsDeleted(db_index=True, default=False, help_text= 'Is this Model record deleted ?', verbose_name= 'Is Deleted')),
                ('created_at', Core.fields.DateFields.CreatedAt(auto_now_add=True, help_text= 'When this Model record was created', null=True, verbose_name= 'Created At')),
                ('modified_at', Core.fields.DateFields.ModifiedAt(auto_now=True, help_text= 'When this Model record was modified', null=True, verbose_name= 'Modified At')),
                ('brand_id', Core.fields.ForeignKeys.ForeignKeyBrand(blank=True, help_text= 'Product of this Brand record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'productbrands', to= 'Products.brand', verbose_name= 'Brand`s Product')),
                ('product_id', Core.fields.ForeignKeys.ForeignKeyProduct(blank=True, help_text= 'Product of this Brand record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'productbrands', to= 'Products.product', verbose_name= 'Brand`s Product')),
            ],
            options={
                'verbose_name': 'Product Brand',
                'verbose_name_plural': 'Products and Brands',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=Core.fields.ManyToMany.ManyToManyBrand(blank=True, db_index=True, help_text= 'Brand of this Product record', related_name= 'product_brand', through= 'Products.ProductBrand', to= 'Products.brand', verbose_name= 'Product`s Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=Core.fields.ManyToMany.ManyToManyCategory(blank=True, db_index=True, help_text= 'Category of this Product record', related_name= 'product_category', through= 'Products.ProductCategory', to= 'Products.category', verbose_name= 'Product`s Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='comment',
            field=Core.fields.ForeignKeys.ForeignKeyComment(blank=True, help_text= 'Comment of this Product record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name= 'products', to= 'Products.comment', verbose_name= 'Product`s Comment'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=Core.fields.ManyToMany.ManyToManyTag(blank=True, db_index=True, help_text= 'Tag of this Product record', related_name= 'product_tag', through= 'Products.ProductTag', to= 'Products.tag', verbose_name= 'Product`s Tag'),
        ),
    ]
