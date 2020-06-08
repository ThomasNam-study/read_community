from django.contrib import admin

# Register your models here.
from board.models import Board
from fcuser.models import Fcuser


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Board, BoardAdmin)
