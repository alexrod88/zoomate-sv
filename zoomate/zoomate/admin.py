from django.contrib import admin

from zoomate.models import Pet, Parent

class ParentAdmin(admin.ModelAdmin):
    list_display = ('category', 'gender', 'race', 'certificate',)

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender', 'race', 'certificate', 'father')

admin.site.register(Parent, ParentAdmin)
admin.site.register(Pet, PetAdmin)
