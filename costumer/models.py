from django.db import models
import core.models

# Create your models here.
class ProfileCostumer(core.models.ProfileBase):
    pass

class Cart(core.models.CoreModel):
    pass

class CartItem(core.models.CoreModel):
    pass

class CostumerCouponList(core.models.CoreModel):
    pass

class Favorite(core.models.CoreModel):
    pass

class FavoriteItem(core.models.CoreModel):
    pass

class WishList(core.models.CoreModel):
    pass

class WishListItem(core.models.CoreModel):
    pass

