from Core.admin import BaseAdminInlineRender, BaseAdminSlug

# MODEL_NAME


# Address

class Address(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Coupon

class Coupon(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Discount

class Discount(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Gallery

class Gallery(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Image

class Image(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Order

class Order(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# OrderItem

class OrderItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Payment

class Payment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Wallet

class Wallet(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# Shipment

class Shipment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# ShipmentItem

class ShipmentItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

# ContactUs

class ContactUs(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = []
    list_filter = []
    list_editable = []
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {
        'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    # prepopulated_fields = {
    #     'slug': ('name',),
    #     }
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""




