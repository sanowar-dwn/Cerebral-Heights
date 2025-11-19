from django.contrib import admin
from .models import Subject, IndexBanner, SiteConfig

# Register your models here.
admin.site.register(Subject)
admin.site.register(IndexBanner)


# Register your models here.
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow add only if no instance exists
        return not SiteConfig.objects.exists()
