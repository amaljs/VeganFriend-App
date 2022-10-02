from django.contrib import admin
from .models import Organ,VeganFood

# Register your models here.

class OrganAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Organ,OrganAdmin)

class VeganAdmin(admin.ModelAdmin):
    list_display = ['name','slug','image','organ']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(VeganFood,VeganAdmin)