from django.contrib import admin
from .models import Property, PropertyType, Feature, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'status', 'district', 'is_featured')
    list_filter = ('status', 'property_type', 'district', 'is_featured')
    search_fields = ('title', 'description', 'address', 'district')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PropertyImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'property_type', 'features')
        }),
        ('Location', {
            'fields': ('address', 'city', 'district', 'postal_code')
        }),
        ('Property Details', {
            'fields': ('price', 'size', 'rooms', 'bathrooms', 'floor', 'year_built')
        }),
        ('Status', {
            'fields': ('status', 'is_featured')
        }),
    )

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)
