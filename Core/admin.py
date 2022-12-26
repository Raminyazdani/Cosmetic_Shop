from django.contrib import admin

# Register your models here.

@admin.action(description='Soft Delete selected objects')
def soft_delete_users(modeladmin, request, queryset):
    queryset.update(is_delete=True)


class BaseAdmin(admin.ModelAdmin):

    actions = [soft_delete_users]

    def get_queryset(self, request):
        # use our manager, rather than the default one
        qs = self.model.objects.get_all()

        # we need this from the superclass method
        ordering = self.ordering or ()  # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
