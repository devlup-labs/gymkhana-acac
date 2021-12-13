from django.contrib import admin
from .models import Board, Society, SocialLink, Senate, SenateMembership, Activity, Contact


class MembershipInline(admin.StackedInline):
    model = SenateMembership
    can_delete = True
    verbose_name_plural = 'Members'


class SenateAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "year")}
    list_display = ('name', 'is_active', 'year')
    list_filter = ('year', 'is_active')


class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'board__name']
    list_display = ('__str__', 'board', 'stype', 'published')
    list_filter = ('published', 'stype')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'society')


# iterable list
main_models = [
    SocialLink,
    Contact
]

admin.site.register(Society, SocietyAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Senate, SenateAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(main_models)
