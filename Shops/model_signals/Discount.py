# import re
#
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.utils.text import slugify
#
# from Core.signals import initial_pre_save
# from Core.utils.ProjectUtils import CustomRegex
# from Customers.models import Customer
# from Markets.models import Market
# from Users.model_signals.Funcs import send_sms, set_permission
# from Users.models import User
#
# # todo do this check post and pre
#
# @receiver(pre_save, sender = User)
# def check_pre_user(sender, instance, **kwargs):
#     initial_pre_save(instance, User, {
#         "phone_number": instance.phone_number
#         })
#
#     regex = re.compile(CustomRegex.phone_regex)
#     instance.phone_number = regex.match(instance.phone_number).group(2)
#     instance.slug = slugify(instance.phone_number)
#     if instance.is_verified == False:
#         send_sms(instance.phone_number)
#     if instance.market is None and instance.is_market == True:
#         market = Market.objects.create(user = instance)
#         instance.market = market
#     if instance.is_market == False:
#         instance.market.is_deleted = True
#         instance.market.save()
#
#     if instance.customer is None and instance.is_customer == True:
#         customer = Customer.objects.create(user = instance)
#         instance.customer = customer
#     if instance.is_customer == False:
#         instance.customer.is_deleted = True
#         instance.customer.save()
#
# @receiver(post_save, sender = User)
# def set_permission_groups(sender, instance, created, **kwargs):
#     set_permission(instance)  # redis_show(instance)
