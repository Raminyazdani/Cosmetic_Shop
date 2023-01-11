def AdminProperty_maker(File, Models, App_name, Scope_parent, Option):
    result = []
    header = f"""
from Core.admin import BaseAdminInlineRender, BaseAdminSlug

"""

    with open(File, "w") as f:
        f.write(header)
        for Model in Models:
            body = f"""
class {Model.capitalize()}(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
"""

            body += r"""
    
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
    prepopulated_fields = #     'slug' : ('name',),#     
    readonly_fields = []
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
    
"""

        f.write(body)
        result.append(f"{App_name:10}.{Model.capitalize():>25}\t {'AdminProperty':25} \t\tadded in AdminProperty.py")

    return result
