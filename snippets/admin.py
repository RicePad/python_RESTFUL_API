from django.contrib import admin
from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


admin.site.register(Snippet, SnippetAdmin)
