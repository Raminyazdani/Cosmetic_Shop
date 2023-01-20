# Generated by Django 4.1.4 on 2023-01-20 17:06

import Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties
import Core.fields.BigAutos.Id
import Core.fields.BigIntegers.ObjectId
import Core.fields.Booleans.IsDelete
import Core.fields.Chars.AltText
import Core.fields.Chars.CardNumber
import Core.fields.Chars.City
import Core.fields.Chars.Coordinate
import Core.fields.Chars.Country
import Core.fields.Chars.FirstName
import Core.fields.Chars.LastName
import Core.fields.Chars.PostalCode
import Core.fields.Chars.Province
import Core.fields.Chars.Sheba
import Core.fields.Chars.Title
import Core.fields.ContentTypes.ContentType
import Core.fields.DateTimes.CreatedAt
import Core.fields.DateTimes.DateFrom
import Core.fields.DateTimes.DateTo
import Core.fields.DateTimes.ModifiedAt
import Core.fields.Decimals.Amount
import Core.fields.Decimals.FinalPrice
import Core.fields.Decimals.MaximumAmount
import Core.fields.Decimals.MinimumAmount
import Core.fields.Emails.Email
import Core.fields.FilePaths.PathOriginal
import Core.fields.FilePaths.PathThumbnail
import Core.fields.Files.Image
import Core.fields.ForeignKeys.GalleryForeignKey
import Core.fields.ForeignKeys.ImageForeignKey
import Core.fields.ForeignKeys.OrderCustomerForeignKey
import Core.fields.ForeignKeys.OrderForeignKey
import Core.fields.ForeignKeys.OrderItemForeignKey
import Core.fields.GenericForeignKeys.Object
import Core.fields.ManyToManys.GalleryManyToMany
import Core.fields.ManyToManys.ImageManyToMany
import Core.fields.PositiveIntegers.DiscountType
import Core.fields.PositiveIntegers.PaymentType
import Core.fields.PositiveIntegers.Percentage
import Core.fields.PositiveIntegers.Quantity
import Core.fields.PositiveIntegers.ShipmentType
import Core.fields.PositiveIntegers.StatusOrder
import Core.fields.PositiveIntegers.StatusPayment
import Core.fields.PositiveIntegers.StatusShipment
import Core.fields.Texts.AddressLine
import Core.fields.Texts.Body
import Core.fields.Texts.Description
import Core.utils.ProjectUtils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Customers', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('firstname', Core.fields.Chars.FirstName.FirstName(blank=True, help_text='Firstname of this Contactus record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Contactus`s Firstname')),
                ('lastname', Core.fields.Chars.LastName.LastName(blank=True, help_text='Lastname of this Contactus record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Contactus`s Lastname')),
                ('title', Core.fields.Chars.Title.Title(help_text='Title of this Contactus record', max_length=20, validators=[django.core.validators.RegexValidator(message='Title must be a valid string with 3 to 20 characters', regex='^.{3,20}$')], verbose_name='Contactus`s Title')),
                ('body', Core.fields.Texts.Body.Body(help_text='Body of this Contactus record', max_length=250, validators=[django.core.validators.MinLengthValidator(10, message='Body must be at least 10 characters'), django.core.validators.MaxLengthValidator(250, message='Body must be at most 250 characters')], verbose_name='Contactus`s Body')),
                ('email', Core.fields.Emails.Email.Email(blank=True, help_text='Emails of this Contactus record', max_length=254, null=True, validators=[django.core.validators.RegexValidator(message='Must be an email)', regex="^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\\.[a-zA-Z0-9-]+)*$")], verbose_name='Contactus`s Emails')),
            ],
            options={
                'verbose_name': 'Contactus',
                'verbose_name_plural': 'Contactuss',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.ContactusMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('discount_type', Core.fields.PositiveIntegers.DiscountType.DiscountType(choices=[(0, 'Percent'), (1, 'Amount')], db_index=True, default=0, help_text='DiscountType of this Discount record', validators=[django.core.validators.MinValueValidator(0, message='Discount type must be at least 0'), django.core.validators.MaxValueValidator(1, message='Discount type must be at most 1')], verbose_name='Discount`s DiscountType')),
                ('minimum_amount', Core.fields.Decimals.MinimumAmount.MinimumAmount(db_index=True, decimal_places=2, default=0.0, help_text='MinimumAmount of this Discount record', max_digits=10, verbose_name='Discount`s MinimumAmount')),
                ('maximum_amount', Core.fields.Decimals.MaximumAmount.MaximumAmount(db_index=True, decimal_places=2, default=0.0, help_text='MaximumAmount of this Discount record', max_digits=10, verbose_name='Discount`s MaximumAmount')),
                ('percentage', Core.fields.PositiveIntegers.Percentage.Percentage(db_index=True, default=0, help_text='Percentage of this Discount record', validators=[django.core.validators.MinValueValidator(0, message='Percent must be at least 0'), django.core.validators.MaxValueValidator(100, message='Percent must be at most 100')], verbose_name='Discount`s Percentage')),
                ('date_from', Core.fields.DateTimes.DateFrom.DateFrom(blank=True, help_text='DateFrom of this Discount record', null=True, verbose_name='Discount`s DateFrom')),
                ('date_to', Core.fields.DateTimes.DateTo.DateTo(blank=True, help_text='DateTo of this Discount record', null=True, verbose_name='Discount`s DateTo')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.DiscountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.GalleryMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('gallery_id', Core.fields.ForeignKeys.GalleryForeignKey.GalleryForeignKey(blank=True, help_text='Gallery of this Image record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleryimages', to='Shops.gallery', verbose_name='Image`s Gallery')),
            ],
            options={
                'verbose_name': 'GalleryImage',
                'verbose_name_plural': 'GalleryImages',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.GalleryimageMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('status_order', Core.fields.PositiveIntegers.StatusOrder.StatusOrder(choices=[(0, 'Pending'), (1, 'Cancel'), (2, 'Done')], db_index=True, default=0, help_text='StatusOrder of this Order record', validators=[django.core.validators.MinValueValidator(0, message='Status order must be at least 0'), django.core.validators.MaxValueValidator(2, message='Status order must be at most 2')], verbose_name='Order`s StatusOrder')),
                ('order_customer', Core.fields.ForeignKeys.OrderCustomerForeignKey.OrderCustomerForeignKey(blank=True, help_text='OrderCustomer of this Order record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='Customers.ordercustomer', verbose_name='Order`s OrderCustomer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.OrderMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('amount', Core.fields.Decimals.Amount.Amount(db_index=True, decimal_places=2, default=0.0, help_text='Amount of this Wallet record', max_digits=10, verbose_name='Wallet`s Amount')),
                ('sheba', Core.fields.Chars.Sheba.Sheba(blank=True, help_text='Sheba of this Wallet record', max_length=26, null=True, validators=[Core.utils.ProjectUtils.CustomValidatorsDefs.ShebaValidator, django.core.validators.MinLengthValidator(26, message='Sheba number must be at least 26 characters'), django.core.validators.MaxLengthValidator(26, message='Sheba number must be at most 26 characters')], verbose_name='Wallet`s Sheba')),
                ('card_number', Core.fields.Chars.CardNumber.CardNumber(blank=True, help_text='CardNumber of this Wallet record', max_length=16, null=True, validators=[Core.utils.ProjectUtils.CustomValidatorsDefs.CardValidator, django.core.validators.MinLengthValidator(16, message='Card number must be at least 16 characters'), django.core.validators.MaxLengthValidator(16, message='Card number must be at most 16 characters')], verbose_name='Wallet`s CardNumber')),
                ('firstname', Core.fields.Chars.FirstName.FirstName(blank=True, help_text='Firstname of this Wallet record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Wallet`s Firstname')),
                ('lastname', Core.fields.Chars.LastName.LastName(blank=True, help_text='Lastname of this Wallet record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Wallet`s Lastname')),
                ('object_id', Core.fields.BigIntegers.ObjectId.ObjectId(blank=True, default=None, help_text='ObjectId of this Wallet record', null=True, verbose_name='Wallet`s ObjectId')),
                ('object', Core.fields.GenericForeignKeys.Object.Object(blank=True, default=None, help_text='ObjectId of this Wallet record', null=True, verbose_name='Wallet`s ObjectId')),
                ('content_type', Core.fields.ContentTypes.ContentType.ContentType(blank=True, default=None, help_text='ContentType of this Wallet record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wallet', to='contenttypes.contenttype', verbose_name='Wallet`s ContentType')),
            ],
            options={
                'verbose_name': 'Wallet',
                'verbose_name_plural': 'Wallets',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.WalletMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('shipment_type', Core.fields.PositiveIntegers.ShipmentType.ShipmentType(choices=[(0, 'Fast'), (1, 'Normal')], db_index=True, default=0, help_text='ShipmentType of this Shipment record', validators=[django.core.validators.MinValueValidator(0, message='Shipment type must be at least 0'), django.core.validators.MaxValueValidator(1, message='Shipment type must be at most 1')], verbose_name='Shipment`s ShipmentType')),
                ('status_shipment', Core.fields.PositiveIntegers.StatusShipment.StatusShipment(choices=[(0, 'Pending'), (1, 'Cancel'), (2, 'Done')], db_index=True, default=0, help_text='StatusShipment of this Shipment record', validators=[django.core.validators.MinValueValidator(0, message='Status shipment must be at least 0'), django.core.validators.MaxValueValidator(2, message='Status shipment must be at most 2')], verbose_name='Shipment`s StatusShipment')),
                ('order_customer', Core.fields.ForeignKeys.OrderCustomerForeignKey.OrderCustomerForeignKey(blank=True, help_text='OrderCustomer of this Shipment record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipments', to='Customers.ordercustomer', verbose_name='Shipment`s OrderCustomer')),
            ],
            options={
                'verbose_name': 'Shipment',
                'verbose_name_plural': 'Shipments',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.ShipmentMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('payment_type', Core.fields.PositiveIntegers.PaymentType.PaymentType(choices=[(0, 'Online'), (1, 'At Place')], db_index=True, default=0, help_text='PaymentType of this Payment record', validators=[django.core.validators.MinValueValidator(0, message='Payment type must be at least 0'), django.core.validators.MaxValueValidator(1, message='Payment type must be at most 1')], verbose_name='Payment`s PaymentType')),
                ('amount', Core.fields.Decimals.Amount.Amount(db_index=True, decimal_places=2, default=0.0, help_text='Amount of this Payment record', max_digits=10, verbose_name='Payment`s Amount')),
                ('description', Core.fields.Texts.Description.Description(blank=True, help_text='Description of this Payment record', max_length=1000, null=True, validators=[django.core.validators.MinLengthValidator(10, message='Description must be at least 10 characters'), django.core.validators.MaxLengthValidator(1000, message='Description must be at most 1000 characters')], verbose_name='Payment`s Description')),
                ('status_payment', Core.fields.PositiveIntegers.StatusPayment.StatusPayment(choices=[(0, 'Pending'), (1, 'Cancel'), (2, 'Paid')], db_index=True, default=0, help_text='StatusPayment of this Payment record', validators=[django.core.validators.MinValueValidator(0, message='Status payment must be at least 0'), django.core.validators.MaxValueValidator(2, message='Status payment must be at most 2')], verbose_name='Payment`s StatusPayment')),
                ('object_id', Core.fields.BigIntegers.ObjectId.ObjectId(blank=True, default=None, help_text='ObjectId of this Payment record', null=True, verbose_name='Payment`s ObjectId')),
                ('object', Core.fields.GenericForeignKeys.Object.Object(blank=True, default=None, help_text='ObjectId of this Payment record', null=True, verbose_name='Payment`s ObjectId')),
                ('content_type', Core.fields.ContentTypes.ContentType.ContentType(blank=True, default=None, help_text='ContentType of this Payment record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='contenttypes.contenttype', verbose_name='Payment`s ContentType')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.PaymentMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('quantity', Core.fields.PositiveIntegers.Quantity.Quantity(db_index=True, default=0, help_text='Order of this Item record', validators=[django.core.validators.MinValueValidator(0, message='Quantity must be at least 0')], verbose_name='Item`s Order')),
                ('final_price', Core.fields.Decimals.FinalPrice.FinalPrice(db_index=True, decimal_places=2, default=0.0, help_text='Order of this Item record', max_digits=10, verbose_name='Item`s Order')),
                ('order', Core.fields.ForeignKeys.OrderForeignKey.OrderForeignKey(blank=True, help_text='Order of this Item record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitems', to='Shops.order', verbose_name='Item`s Order')),
                ('order_customer', Core.fields.ForeignKeys.OrderCustomerForeignKey.OrderCustomerForeignKey(blank=True, help_text='Order of this Item record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitems', to='Customers.ordercustomer', verbose_name='Item`s Order')),
            ],
            options={
                'verbose_name': 'Orderitem',
                'verbose_name_plural': 'Orderitems',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.OrderitemMixin, models.Model),
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=Core.fields.ForeignKeys.OrderItemForeignKey.OrderItemForeignKey(blank=True, help_text='OrderItem of this Order record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='Shops.orderitem', verbose_name='Order`s OrderItem'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('path_original', Core.fields.FilePaths.PathOriginal.PathOriginal(help_text='PathOriginal of this Image record', path='PATHORIGINAL/', recursive=True, verbose_name='Image`s PathOriginal')),
                ('path_thumbnail', Core.fields.FilePaths.PathThumbnail.PathThumbnail(help_text='PathThumbnail of this Image record', path='PATHTHUMBNAIL/', recursive=True, verbose_name='Image`s PathThumbnail')),
                ('image', Core.fields.Files.Image.Image(help_text='Image of this Image record', upload_to='IMAGE/', verbose_name='Image`s Image')),
                ('alt_text', Core.fields.Chars.AltText.AltText(help_text='AltText of this Image record', max_length=30, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Image`s AltText')),
                ('gallery', Core.fields.ManyToManys.GalleryManyToMany.GalleryManyToMany(blank=True, db_index=True, help_text='Gallery of this Image record', related_name='images', through='Shops.GalleryImage', to='Shops.gallery', verbose_name='Image`s Gallery')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.ImageMixin, models.Model),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='image_id',
            field=Core.fields.ForeignKeys.ImageForeignKey.ImageForeignKey(blank=True, help_text='Gallery of this Image record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleryimages', to='Shops.image', verbose_name='Image`s Gallery'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=Core.fields.ManyToManys.ImageManyToMany.ImageManyToMany(blank=True, db_index=True, help_text='Image of this Gallery record', related_name='gallerys', through='Shops.GalleryImage', to='Shops.image', verbose_name='Gallery`s Image'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', Core.fields.BigAutos.Id.Id(db_index=True, help_text='Id of this Model record', primary_key=True, serialize=False, verbose_name='Model`s Id')),
                ('is_delete', Core.fields.Booleans.IsDelete.IsDelete(db_index=True, default=False, help_text='Is this Model record has deleted ?', verbose_name='Is Delete')),
                ('created_at', Core.fields.DateTimes.CreatedAt.CreatedAt(auto_now_add=True, help_text='CreatedAt of this Model record', null=True, verbose_name='Model`s CreatedAt')),
                ('modified_at', Core.fields.DateTimes.ModifiedAt.ModifiedAt(auto_now=True, help_text='ModifiedAt of this Model record', null=True, verbose_name='Model`s ModifiedAt')),
                ('country', Core.fields.Chars.Country.Country(blank=True, help_text='Country of this Address record', max_length=30, null=True, verbose_name='Address`s Country')),
                ('city', Core.fields.Chars.City.City(blank=True, help_text='City of this Address record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Must be a valid city name)', regex='^[a-zA-Z]{3,30}$')], verbose_name='Address`s City')),
                ('province', Core.fields.Chars.Province.Province(blank=True, help_text='Province of this Address record', max_length=30, null=True, verbose_name='Address`s Province')),
                ('address_line', Core.fields.Texts.AddressLine.AddressLine(blank=True, help_text='AddressLine of this Address record', max_length=500, null=True, validators=[django.core.validators.RegexValidator(message='Must be a valid address)', regex='^\\w.{3,499}$')], verbose_name='Address`s AddressLine')),
                ('postal_code', Core.fields.Chars.PostalCode.PostalCode(blank=True, help_text='PostalCode of this Address record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Must be a valid postal code)', regex='^\\d{5}-\\d{5}$')], verbose_name='Address`s PostalCode')),
                ('firstname', Core.fields.Chars.FirstName.FirstName(blank=True, help_text='Firstname of this Address record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Address`s Firstname')),
                ('lastname', Core.fields.Chars.LastName.LastName(blank=True, help_text='Lastname of this Address record', max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='must be a valid name with 3 to 30 characters', regex='^.{3,30}$')], verbose_name='Address`s Lastname')),
                ('Coordinate', Core.fields.Chars.Coordinate.Coordinate(blank=True, help_text='Coordination of this Address record', max_length=21, null=True, validators=[django.core.validators.RegexValidator(message='Must be a valid coordinate)', regex='^(?:[-+]?[1-8]?\\d(?:\\.\\d{0,7})?|90(?:\\.0{0,7})?),(?:[-+]?(?:180(?:\\.0{0,7})?|(?:(?:1[0-7]\\d)|(?:[1-9]?\\d))(?:\\.\\d{0,7})?))$')], verbose_name='Address`s Coordination')),
                ('object_id', Core.fields.BigIntegers.ObjectId.ObjectId(blank=True, default=None, help_text='ObjectId of this Address record', null=True, verbose_name='Address`s ObjectId')),
                ('object', Core.fields.GenericForeignKeys.Object.Object(blank=True, default=None, help_text='ObjectId of this Address record', null=True, verbose_name='Address`s ObjectId')),
                ('content_type', Core.fields.ContentTypes.ContentType.ContentType(blank=True, default=None, help_text='ContentType of this Address record', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to='contenttypes.contenttype', verbose_name='Address`s ContentType')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
            bases=(Core.ProjectMixins.Apps.Shops_Mixins.ModelRequiredProperties.AddressMixin, models.Model),
        ),
    ]
