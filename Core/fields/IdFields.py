from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField

class CustomIdField(CustomDefaultField.BigAutoField):
    """
    Custom ID Field as BigAutoField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "ID",


        }

    def __init__(self, *args, **kwargs):

        for key, value in CustomIdField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Id of this {kwargs['class_name']} record"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs["class_name"] + "`s Id"))
        super().__init__(*args, **kwargs)


# Add your custom gallery field  # gallery = models.OneToOneField("Gallery", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Gallery"),help_text=_("Gallery of the product"))
