import random

import redis
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType

from Cosmetic_Shop.RedisConfig import redis_config

def send_sms(phone_number):
    temp = []
    for i in range(6):
        temp.append(random.randint(0,9))
    code = "".join([str(x) for x in temp])

    redis.Redis(**redis_config).set(phone_number,code)
    redis.Redis(**redis_config).expire(phone_number, 60)

def set_permission(instance):
    try:
        groups = Group.objects.all()
    except:
        groups = None
    groups_list = ["viewer","manager","operator"]
    for g in groups_list:
        if g not in [x.name for x in groups]:
            Group.objects.create(name=f'{g}')

    if instance.is_market:
        if "operator" not in [x.name for x in instance.groups.all()]:
            instance.groups.add(Group.objects.get(name="operator"))
    else:
        if "operator" in [x.name for x in instance.groups.all()]:
            instance.groups.remove(Group.objects.get(name="operator"))
    if instance.is_admin:
        if "manager" not in [x.name for x in instance.groups.all()]:
            instance.groups.add(Group.objects.get(name="manager"))
    else:
        if "manager" in [x.name for x in instance.groups.all()]:
            instance.groups.remove(Group.objects.get(name="manager"))
    if instance.is_customer:
        if "viewer" not in [x.name for x in instance.groups.all()]:
            instance.groups.add(Group.objects.get(name="viewer"))
    else:
        if "viewer" in [x.name for x in instance.groups.all()]:
            instance.groups.remove(Group.objects.get(name="viewer"))

def redis_show(instance):
    print(redis.Redis(**redis_config).get(instance.phone_number))
