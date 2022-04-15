from django.contrib import admin

# Register your models here.
from TestModel.models import *
 
class TagInline(admin.TabularInline):
    model = Tag
 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]
 
    )
 
admin.site.register(Contact, ContactAdmin)

# Register your models here.
admin.site.register([testmodel,Tag])