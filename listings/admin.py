from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_filter = ('realtor',)
    list_display = ('id', 'title', 'price', 'is_published', 'realtor')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'address', 'city', 'price')
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)