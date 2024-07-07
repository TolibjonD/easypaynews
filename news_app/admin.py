from django.contrib import admin
from news_app.models import Category, News, Contact

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'status']
    list_filter = ['status', 'created_at', "published_at"]
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'published_at'
    search_fields = ['title', 'body']
    ordering = ['published_at', 'status']


admin.site.register(Contact)