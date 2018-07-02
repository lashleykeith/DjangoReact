from django.contrib import admin
from band.models import Band
# Register your models here.

class BandAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']

admin.site.register(Band, BandAdmin)