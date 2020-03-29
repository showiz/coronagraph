from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class ChileDataAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

admin.site.register(ChileData, ChileDataAdmin)

class LinksAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

admin.site.register(Links, LinksAdmin)

class RegionsAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

admin.site.register(Regions, RegionsAdmin)

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Page, PageAdmin)

class WorldAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(World, WorldAdmin)

class ChileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Chile, ChileAdmin)
