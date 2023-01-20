import re

from django.utils.translation import gettext_lazy as _

class DelClassName:

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        res = re.findall('[A-Z][^A-Z]*', kwargs["class_name"])
        if len(res) > 1: kwargs["class_name"], kwargs["field_name"] = res[1], res[0]

        kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs['class_name'] + f"`s {kwargs['field_name']}"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"{kwargs['field_name']} of this {kwargs['class_name']} record"))

        del kwargs["class_name"], kwargs['field_name'],

        super().__init__(*args, **kwargs)

class Base(DelClassName):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
