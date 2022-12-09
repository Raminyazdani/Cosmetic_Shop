from django.db import models
import core.models


# Create your models here.
class OrderItem(core.models.CoreModel):
    pass


class OrderMarket(core.models.OrderBase):
    pass


class OrderCostumer(core.models.OrderBase):
    pass
