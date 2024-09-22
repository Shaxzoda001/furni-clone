from django.contrib import admin
from .models import About, Shop, Service, Blog


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_title')
    search_fields = ('title', 'icon_title')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date', 'slug')
    search_fields = ('title', 'slug')
    list_filter = ('created_date', 'price')
    ordering = ('-created_date',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_date')
    search_fields = ('title', 'user__username')
    list_filter = ('created_date', 'user')
    ordering = ('-created_date',)
