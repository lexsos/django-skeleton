from django.contrib import admin

from .models import TestModel


class TestAdmin(admin.ModelAdmin):

    list_filter = ('title', 'enabled')
    list_display = ('title', 'enabled', 'weight')


admin.site.register(TestModel, TestAdmin)
