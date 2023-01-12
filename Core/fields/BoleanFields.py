from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField

class BooleanABC(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Abstract Is Available Field
    """

    class_custom_default_attrs = {
        "class_name": "Model", # in this # required
        "field_name": "ABCBoolean", # in this # required
        "null": False, # in super
        "blank": False, # in super
        "default": False, # in super
        "db_index": False, # in super
        # custom help text in init # in this # optional
        # custom verbose name in init # in this # optional
        }

    def __init__(self, *args, **kwargs):
        for key, value in BooleanABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record ... ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs['class_name'] + "`s ..."))

        super().__init__(*args, **kwargs)

class IsAvailable(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Available Field as BooleanField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": True,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsAvailable.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record available ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs['class_name'] + "`s availability"))

        super().__init__(*args, **kwargs)

class IsActive(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Active Field as BooleanField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": True,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsActive.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record available ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs['class_name'] + "`s availability"))

        super().__init__(*args, **kwargs)

class IsDeleted(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Deleted Field as BooleanField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsDeleted.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record deleted ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Deleted"))

        super().__init__(*args, **kwargs)

class IsCustomer(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Deleted Field as BooleanField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,  # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsCustomer.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record has costumer profile ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Costumer"))

        super().__init__(*args, **kwargs)

class IsMarket(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Market Field as BooleanField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsMarket.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record has market profile ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Market"))

        super().__init__(*args, **kwargs)

class IsStaff(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Staff Field as BooleanField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsStaff.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record has staff permissions ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Staff"))

        super().__init__(*args, **kwargs)

class IsAdmin(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Admin Field as BooleanField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsAdmin.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record has admin permissions ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Admin"))

        super().__init__(*args, **kwargs)

class IsSuperUser(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Super User Field as BooleanField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsSuperUser.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record has super user permissions ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Super User"))

        super().__init__(*args, **kwargs)

class IsVerified(CustomDefaultField.BooleanField):
    class Meta:
        abstract=True
    """
    Custom Is Verified Field as BooleanField
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "is available",
        "default": False,
        "db_index": True,
        # custom help text in init
        # custom verbose name in init
        }

    def __init__(self, *args, **kwargs):
        for key, value in IsVerified.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record verified ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Verified"))

        super().__init__(*args, **kwargs)
