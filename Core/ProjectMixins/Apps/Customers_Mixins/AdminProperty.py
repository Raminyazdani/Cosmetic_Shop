
from Core.admin import BaseAdminInlineRender, BaseAdminSlug


class Customer(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Cart(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Cartitem(BaseAdminInlineRender, BaseAdminSlug):
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
    prepopulated_fields = {}  # 'slug' : ('name',),#
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

class CustomerCoupon(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Favorite(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Favoriteitem(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Ordercustomer(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Wishlist(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Wishlistitem(BaseAdminInlineRender, BaseAdminSlug):
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
    
