from django.contrib import admin
from .models import Direction, Application, Viloyat, Tuman
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
admin.site.register(Direction)
admin.site.register(Viloyat)
admin.site.register(Tuman)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'manzil', 'phone', 'status', 'created_at')
    list_filter = ('status', 'viloyat', 'tuman', 'created_at')
    search_fields = ('first_name', 'last_name', 'father_name', 'phone', 'yashash_joyi')
    readonly_fields = ('created_at', 'manzil')

    def manzil(self, obj):
        return f"{obj.viloyat.nomi}, {obj.tuman.nomi}, {obj.yashash_joyi}"
    manzil.short_description = 'Manzil'

    def pdf_link(self, obj):
        url = reverse('application_pdf', args=[obj.pk])
        return format_html('<a href="{}" target="_blank">PDF yuklab olish</a>', url)
    pdf_link.short_description = 'PDF'
