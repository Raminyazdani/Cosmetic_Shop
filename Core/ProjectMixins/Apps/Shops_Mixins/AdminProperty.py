
from Core.admin import BaseAdminInlineRender, BaseAdminSlug


class Address(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Coupon(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Discount(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Gallery(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Image(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Galleryimage(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Order(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Orderitem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Payment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Wallet(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Shipment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    

class Contactus(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    
    list_display = []
    list_filter = []
    list_editable =[]
    ordering = []
    filter_horizontal = []
    fieldsets = (("Profiling", {'classes': ('extrapretty',),
        'fields': ()
        }), ("Extras", {'fields': (),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {'fields': (),
        'classes': ('wide',)
        }), ("time", {'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {}#     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    
