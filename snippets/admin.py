from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import ProgrammingLanguage, Snippet

admin.site.register(ProgrammingLanguage)

@admin.register(Snippet)
class SnippetsAdmin(MarkdownxModelAdmin):
  class Media:
    css = {
      'all': ('markdownx.css')
    }