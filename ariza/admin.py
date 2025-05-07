from django.contrib import admin
from .models import Direction, Application
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
admin.site.register(Direction)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'direction', 'created_at', 'pdf_link')
    def pdf_link(self, obj):
        url = reverse('application_pdf', args=[obj.pk])
        return format_html('<a href="{}" target="_blank">PDF yuklab olish</a>', url)
    pdf_link.short_description = 'PDF'

admin.site.register(Application, ApplicationAdmin)
