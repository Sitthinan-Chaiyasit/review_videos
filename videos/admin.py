from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'order', 'created_at']
    list_editable = ['is_featured', 'order']
    list_filter = ['category', 'is_featured']
    search_fields = ['title', 'description']