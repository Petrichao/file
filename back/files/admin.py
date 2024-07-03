from django.contrib import admin

from files.models import File, Word


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


class WordAdmin(admin.ModelAdmin):
    list_display = (
        'word',
        'tf',
        'df',
        'idf',
        'get_file_count'
    )
    search_fields = (
        'word',
        'tf',
        'df',
        'idf',
    )

    def get_file_count(self, obj):
        return obj.it_is_found_in.count()

    get_file_count.short_description = 'Количество тегов'  

    empty_value_display = '--пусто--'


admin.site.register(Word, WordAdmin)
admin.site.register(File, FileAdmin)
