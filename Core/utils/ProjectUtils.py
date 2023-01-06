from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, MinLengthValidator, \
    MaxLengthValidator
from django.utils.translation import gettext_lazy as _


class CustomRegex:
    phone_regex = r'^(\+98|\+980|0098|00980|0|)\d{10}$'
    name_regex = r'^.{3,30}$'
    title_regex = r'^.{3,20}$'



class CustomValidators:
    RatingValidator = [MinValueValidator(0, message=_('Rating must be at least 0')),
                       MaxValueValidator(10, message=_('Rating must be at most 10'))]
    PhoneValidator = [RegexValidator(regex=CustomRegex.phone_regex, message=_('must be a phone number with 10 digits'))]
    NameValidator = [
        RegexValidator(regex=CustomRegex.name_regex, message=_('must be a valid name with 3 to 30 characters'))]
    GenderValidator = [MinValueValidator(0, message=_('Gender is integer ,must be at least 0')),
                       MaxValueValidator(2, message=_('Gender is integer ,must be at most 2'))]
    ShortDescriptionValidator = [MinLengthValidator(3, message=_('Short description must be at least 3 characters')),
                                 MaxLengthValidator(100, message=_('Short description must be at most 100 characters'))]
    DescriptionValidator = [MinLengthValidator(10, message=_('Description must be at least 10 characters')),
                            MaxLengthValidator(1000, message=_('Description must be at most 1000 characters'))]
    PriceValidator = [MinValueValidator(0, message=_('Price must be at least 0')),
                      MaxValueValidator(1000000000, message=_('Price must be at most 1000000000'))]
    TitleValidator = [
        RegexValidator(regex=CustomRegex.title_regex,
                       message=_('Title must be a valid string with 3 to 20 characters'))]
    BodyValidator = [MinLengthValidator(10, message=_('Body must be at least 10 characters')),
                     MaxLengthValidator(250, message=_('Body must be at most 250 characters'))]
