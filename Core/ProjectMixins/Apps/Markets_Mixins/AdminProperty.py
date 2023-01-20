
from Core.admin import BaseAdminInlineRender, BaseAdminSlug


class Market(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Inventory(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Inventoryitem(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Inventoryitemproperty(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Property(BaseAdminInlineRender, BaseAdminSlug):
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
    

class Ordermarket(BaseAdminInlineRender, BaseAdminSlug):
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
    
