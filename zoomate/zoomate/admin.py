from django.contrib import admin

from zoomate.models import Pet, Parent, Adoption, Sale, Categories, Races, Vaccines

class ParentAdmin(admin.ModelAdmin):
    list_display = ('category', 'gender', 'race', 'certificate',)

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender', 'race', 'certificate', 'father')

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('animal', 'owner', 'created_at', 'modified_at')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('animal', 'owner', 'price', 'created_at', 'modified_at')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

class RacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class VaccinesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(Parent, ParentAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Races, RacesAdmin)
admin.site.register(Vaccines, VaccinesAdmin)
