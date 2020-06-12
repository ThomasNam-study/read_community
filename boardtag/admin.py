from django.contrib import admin

# Register your models here.
from boardtag.models import BoardTag


class BoardTagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(BoardTag, BoardTagAdmin)
