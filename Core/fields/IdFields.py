from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField

class AbstractBigAutoField(CustomDefaultField.BigAutoField):
    class Meta:
        abstract=True
    class_custom_default_attrs = {
        "class_name": "Model", # in this # required
        "field_name": "ABCBigAutoField",  # in this # required
        "primary_key": True, # in super
        "db_index": True, # super
        # "auto_created": True, # optional
        # "blank": True, # optional
        # "null": False, # optional
        # "editable": False, # optional
        # custom help text in init # optional
        # custom verbose name in init # optional
        }

    def __init__(self, *args, **kwargs):
        for key, value in AbstractBigAutoField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Id of this {kwargs['class_name']} record"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs["class_name"] + "`s Id"))
        super().__init__(*args, **kwargs)

class CustomIdField(CustomDefaultField.BigAutoField):
    class Meta:
        abstract=True
    """
    Custom ID Field as BigAutoField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "ID",
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomIdField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Id of this {kwargs['class_name']} record"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs["class_name"] + "`s Id"))
        super().__init__(*args, **kwargs)  # Add your custom gallery field  # gallery = models.OneToOneField("Gallery", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Gallery"),help_text=_("Gallery of the product"))
