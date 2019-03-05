from django.contrib import admin

from app.models import *
from api.models import *
admin.site.site_title = 'VALUE MANAGEMENT'
admin.site.site_header = 'VALUE MANAGEMENT'


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'kana', 'mail', 'tel', 'appoint_date', 'link', 'appoint_status')
    search_fields = (
        'first_name',
        'last_name',
        'first_name_kana',
        'last_name_kana',
        'mail',
    )
    fieldsets = (
        (None, {'fields': ('last_name', 'first_name',)}),
        (None, {'fields': ('last_name_kana', 'first_name_kana')}),
        (None, {'fields': ('tel', 'mail')}),
        (None, {'fields': ('place', 'appoint_date', 'appoint_status')}),
    )
    list_editable = ('appoint_status',)
    list_filter = ('appoint_status',)



ClientAdmin.list_display_links = ('name',)


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'client', 'url'
    )


LikeAdmin.list_display_links = ('client',)


class BanquetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'banquet_name'
    )


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'style_name'
    )


class PartyCostumeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'party_costume_name'
    )


class SiteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'site_name'
    )



class PhotoAdmin(admin.ModelAdmin):
    pass


class BeforePhotoAdmin(admin.ModelAdmin):
    pass


class CuisineAdmin(admin.ModelAdmin):
    pass


class CakeAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class CoordinateAdmin(admin.ModelAdmin):
    pass


class EffectAdmin(admin.ModelAdmin):
    pass


class EstimateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Banquet, BanquetAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(PartyCostume, PartyCostumeAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(BeforePhoto, BeforePhotoAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(Effect, EffectAdmin)
admin.site.register(Estimate, EstimateAdmin)
admin.site.register(Site, SiteAdmin)
