from django.contrib import admin
from .models import ProfileUser, Publication, Category
# Register your models here.

class PublicationAdmin(admin.ModelAdmin):
    list_filter = ("publication_date", "category",)
    list_display = ("user", "category", "publication_date",)
    search_fields = ("user","category", )


admin.site.register(Publication, PublicationAdmin)
admin.site.register(ProfileUser)
admin.site.register(Category)