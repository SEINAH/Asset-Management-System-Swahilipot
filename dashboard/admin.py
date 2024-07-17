from django.contrib import admin
from .models import New_Asset, Asset, Maintainance

admin.site.site_header = 'Asset Management Dashboard'

class New_AssetAdmin(admin.ModelAdmin):
    list_display = ('category', 'quantity', 'approved_at')
    list_filter = ('category',)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('category', 'quantity', 'borrowing_time', 'returning_time', 'comment')
    list_filter = ('category',)

class MaintainanceAdmin(admin.ModelAdmin):
    list_display = ('category', 'quantity', 'comment')
    list_filter = ('category',)

# Register your models here.
admin.site.register(New_Asset, New_AssetAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Maintainance, MaintainanceAdmin)
