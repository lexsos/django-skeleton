from django.contrib import admin
from  tinymce.widgets import AdminTinyMCE

from .models import TestModel


class TestAdmin(admin.ModelAdmin):

    list_filter = ('title', 'enabled')
    list_display = ('title', 'enabled', 'weight')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'title':
            kwargs['widget'] = AdminTinyMCE()
        return super(TestAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(TestModel, TestAdmin)
