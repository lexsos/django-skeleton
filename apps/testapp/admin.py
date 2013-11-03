from django.contrib import admin
from dj_mixin.admin import AdminTinymceMixin

from .models import TestModel


class TestAdmin(AdminTinymceMixin, admin.ModelAdmin):

    list_filter = ('title', 'enabled')
    list_display = ('title', 'enabled', 'weight')

    rich_fields = ('title',)

admin.site.register(TestModel, TestAdmin)
