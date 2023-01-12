from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField

class DateTimeABC(CustomDefaultField.DateTimeField):
    class Meta:
        abstract=True
    """
    Custom Created At Field as DateTimeField
    """

    class_custom_default_attrs = {
        "class_name": "Model", # in this # required
        "field_name": "ABCDateTime", # in this # required
        "auto_now": True,   # one of them below # in this # optional
        "auto_now_add": True,  # one of them above # in this # optional
        "blank": False, # in super
        "null": False, # in super
        # custom help text in init # in this # optional
        # custom verbose name in init # in this # optional
        }

    def __init__(self, *args, **kwargs):
        for key, value in DateTimeABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {kwargs['class_name']} record was ..."))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("..."))

        super().__init__(*args, **kwargs)

class CreatedAt(CustomDefaultField.DateTimeField):
    class Meta:
        abstract=True
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
        for key, value in CreatedAt.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {kwargs['class_name']} record was created"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Created At"))

        super().__init__(*args, **kwargs)

class ModifiedAt(CustomDefaultField.DateTimeField):
    class Meta:
        abstract=True
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
        for key, value in ModifiedAt.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {kwargs['class_name']} record was modified"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Modified At"))

        super().__init__(*args, **kwargs)
