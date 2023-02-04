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
# from Users.models import User
#
# # todo do this check post and pre
#
# @receiver(pre_save, sender = Tag)
# def tag_pre_save(sender, instance, *args, **kwargs):
#     initial_pre_save(instance, Tag, {
#         "name": instance.name
#         })
#
#     slug = slugify(instance.name)
#     instance.slug = slug
#
# @receiver(post_save, sender = Tag)
# def Tag_post_save(sender, instance, **kwargs):
#     check_gallery(instance)
#     update_images(instance)