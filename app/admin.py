from django.contrib import admin


from app.models import Client

admin.site.site_title = 'VALUE MANAGEMENT'
admin.site.site_header = 'VALUE MANAGEMENT'

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'kana', 'mail', 'tel', 'date','link')

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name')}),
        (None, {'fields': ('last_name_kana', 'first_name_kana')}),
        (None, {'fields': ('tel', 'mail')}),
        (None, {'fields': ('place', 'date')}),
    )

ClientAdmin.list_display_links = ('name',)


admin.site.register(Client, ClientAdmin)
