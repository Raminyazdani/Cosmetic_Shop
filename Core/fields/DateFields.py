from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField

class CustomCreatedAtField(CustomDefaultField.DateTimeField):
    """
    Custom Created At Field as DateTimeField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "created at",
        "blank": True,
        "null": True,
        "auto_now_add": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):


        for key, value in CustomCreatedAtField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {kwargs['class_name']} record was created"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Created At"))

        super().__init__(*args, **kwargs)

class CustomModifiedAtField(CustomDefaultField.DateTimeField):
    """
    Custom Modified At Field as DateTimeField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "modified at",
        "blank": True,
        "null": True,
        "auto_now": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):


        for key, value in CustomModifiedAtField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {kwargs['class_name']} record was modified"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Modified At"))

        super().__init__(*args, **kwargs)
