from django.contrib import admin

# Register your models here.
from django.forms import models, BaseModelFormSet


@admin.action(description='Soft Delete selected objects')
def soft_delete(modeladmin, request, queryset):
    queryset.update(is_delete=True)


@admin.action(description='Restore selected objects')
def Restore_delete(modeladmin, request, queryset):
    queryset.update(is_delete=False)


class BaseAdmin(admin.ModelAdmin):
    class Meta:
        abstract=True
    actions = [soft_delete, Restore_delete]

    def get_queryset(self, request):
        # use our manager, rather than the default one
        qs = self.model.objects.get_all()

        # we need this from the superclass method
        ordering = self.ordering or ()  # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)

        return qs


class BaseAdminSlug(BaseAdmin):
    class Meta:
        abstract=True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return ['slug'] + list(self.readonly_fields)
        return self.readonly_fields

    class Media:
        js = ("/statics/Base/Admin_statics/Admin_slug.js", "/statics/Base/Admin_statics/jquery.js")


class CategoryAdminSlug(BaseAdmin):
    class Meta:
        abstract=True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return ['slug'] + list(self.readonly_fields)
        return self.readonly_fields

    class Media:
        js = ("/statics/Base/Admin_statics/string_to_slug.js","/statics/Base/Admin_statics/Admin_category_slug.js", "/statics/Base/Admin_statics/jquery.js")



class BaseAdminInlineRender(BaseAdmin):
    class Meta:
        abstract=True

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    class Media:
        js = ("/statics/Base/Admin_statics/Admin_slug.js", "/statics/Base/Admin_statics/jquery.js")


class BaseAdminSlugUser(BaseAdminSlug):
    class Meta:
        abstract=True
    class Media:
        js = ("/statics/Base/Admin_statics/Admin_user_slug.js", "/statics/Base/Admin_statics/jquery.js")


class BaseFormSetInlineNoDelete(models.BaseInlineFormSet):
    class Meta:
        abstract=True
    def __init__(self, *args, **kwargs):
        super(BaseFormSetInlineNoDelete, self).__init__(*args, **kwargs)
        self.can_delete = False


class CustomInlineAdmin(admin.TabularInline):
    class Meta:
        abstract=True
    classes = ('collapse',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra


class CustomInlineAdminOneToMany(CustomInlineAdmin):
    class Meta:
        abstract=True
    formset = BaseFormSetInlineNoDelete


class CustomStackedAdmin(admin.StackedInline):
    class Meta:
        abstract=True
    classes = ('collapse',)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra
