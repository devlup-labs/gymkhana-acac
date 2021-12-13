from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'author', 'society', 'date')
    list_filter = ('date',)

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
