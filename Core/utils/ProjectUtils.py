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
    DollarPriceValidator = [MinValueValidator(0, message=_('Price must be at least 0')),
                            MaxValueValidator(1000000000, message=_('Price must be at most 1000000000'))]
    TitleValidator = [
        RegexValidator(regex=CustomRegex.title_regex,
                       message=_('Title must be a valid string with 3 to 20 characters'))]
    BodyValidator = [MinLengthValidator(10, message=_('Body must be at least 10 characters')),
                     MaxLengthValidator(250, message=_('Body must be at most 250 characters'))]

class CustomStringMaker:
    class ForeignKey:
        @staticmethod
        def to_gen(app_name,class_model):
            return app_name+'.'+class_model
        @staticmethod
        def related_name_gen(class_name,related_name_default):
            return class_name.lower()+'_'+related_name_default.lower()

    class ManyToMany:
        @staticmethod
        def to_gen(app_name,class_model):
            return app_name+'.'+class_model

        @staticmethod
        def related_name_gen(class_name,related_name_default):
            return class_name.lower()+'_'+related_name_default.lower()

        @staticmethod
        def through_gen(class_name,app_model_name,through_fields=None):
            #       "class_name" :                  "Product",              "Category"
            #       "field_name":                   "Category",             "Product #
            #       "app_name_destination":         "Products",             "Products"
            #       "app_name_model_destination":   "Category",             "Product"
            #       "through_fields":               [None, "category_id"]   ["product_id",None]
            #       "through":                      "ProductCategory",      "ProductCategory"


            if through_fields is None:
                return class_name.capitalize()+app_model_name.capitalize()
            else:
                if through_fields[0] is None:
                    return class_name.capitalize()+app_model_name.capitalize()
                elif through_fields[1] is None:
                    return app_model_name.capitalize()+class_name.capitalize()



        @staticmethod
        def through_fields_gen(class_name,app_model_name,through_fields=None):
            #        "through_fields": ["product_id", None],
            if through_fields is None:
                result = [class_name.lower(), app_model_name.lower()]
            else:
                if through_fields[0] is None:

                    result  = [class_name.lower()+"_id",through_fields[1]]
                elif through_fields[1] is None:
                    result  = [class_name.lower()+"_id",through_fields[0],]
            return result
