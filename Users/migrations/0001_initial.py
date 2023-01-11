# Generated by Django 4.1.4 on 2023-01-11 19:28

import Core.ProjectMixins.Base.AbsoluteUrl
import Core.ProjectMixins.Base.Save
import Core.ProjectMixins.Base.Str
import Core.fields.BoleanFields
import Core.fields.CharFields
import Core.fields.DateFields
import Core.fields.IdFields
import Core.fields.SlugFields
import Users.managers
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', Core.fields.IdFields.CustomIdField(db_index=True, help_text='Id of this User record', primary_key=True, serialize=False, verbose_name='User`s Id')),
                ('phone_number', Core.fields.CharFields.CustomPhoneNumberField(db_index=True, help_text='Phone number of this User record', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='must be a phone number with 10 digits', regex='^(\\+98|\\+980|0098|00980|0|)\\d{10}$')], verbose_name='User`s phone number')),
                ('is_costumer', Core.fields.BoleanFields.CustomIsCustomerField(db_index=True, default=False, help_text='Is this User record has costumer profile ?', verbose_name='Is Costumer')),
                ('is_market', Core.fields.BoleanFields.CustomIsMarketField(db_index=True, default=False, help_text='Is this User record has market profile ?', verbose_name='Is Market')),
                ('is_staff', Core.fields.BoleanFields.CustomIsStaffField(db_index=True, default=False, help_text='Is this User record has staff permissions ?', verbose_name='Is Staff')),
                ('is_active', Core.fields.BoleanFields.CustomIsActiveField(db_index=True, default=True, help_text='Is this User record available ?', verbose_name='User`s availability')),
                ('is_admin', Core.fields.BoleanFields.CustomIsAdminField(db_index=True, default=False, help_text='Is this User record has admin permissions ?', verbose_name='Is Admin')),
                ('is_superuser', Core.fields.BoleanFields.CustomIsSuperUserField(db_index=True, default=False, help_text='Is this User record has super user permissions ?', verbose_name='Is Super User')),
                ('is_verified', Core.fields.BoleanFields.CustomIsVerifiedField(db_index=True, default=False, help_text='Is this User record verified ?', verbose_name='Is Verified')),
                ('slug', Core.fields.SlugFields.CustomSlugField(blank=True, help_text='Slug of this User record', max_length=100, null=True, unique=True, verbose_name='User`s Slug')),
                ('is_delete', Core.fields.BoleanFields.CustomIsDeletedField(db_index=True, default=False, help_text='Is this User record deleted ?', verbose_name='Is Deleted')),
                ('created_at', Core.fields.DateFields.CustomCreatedAtField(auto_now_add=True, help_text='When this User record was created', null=True, verbose_name='Created At')),
                ('modified_at', Core.fields.DateFields.CustomModifiedAtField(auto_now=True, help_text='When this User record was modified', null=True, verbose_name='Modified At')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model, Core.ProjectMixins.Base.Save.SaveName, Core.ProjectMixins.Base.Save.SaveNormal, Core.ProjectMixins.Base.Str.PhoneNumber, Core.ProjectMixins.Base.AbsoluteUrl.UrlId),
            managers=[
                ('objects', Users.managers.CustomBaseUserManager()),
                ('subsets', Users.managers.CustomBaseUserManager()),
            ],
        ),
    ]
