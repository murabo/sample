from django.contrib import admin


from app.models import Client, Like

admin.site.site_title = 'VALUE MANAGEMENT'
admin.site.site_header = 'VALUE MANAGEMENT'

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'kana', 'mail', 'tel', 'appoint_date','link')

    fieldsets = (
        (None, {'fields': ('last_name', 'first_name',)}),
        (None, {'fields': ('last_name_kana', 'first_name_kana')}),
        (None, {'fields': ('tel', 'mail')}),
        (None, {'fields': ('place', 'appoint_date', 'appoint_status')}),
    )

ClientAdmin.list_display_links = ('name',)


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'client', 'url'
    )
LikeAdmin.list_display_links = ('client',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Like, LikeAdmin)
