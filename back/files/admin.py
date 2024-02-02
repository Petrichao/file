from django.contrib import admin

from files.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = (
        'file',
        'uploaded_at',
        'processed'
    )
    search_fields = (
        'file',
        'uploaded_at',
        'processed'
    )
    empty_value_display = '--пусто--'


admin.site.register(File, FileAdmin)
