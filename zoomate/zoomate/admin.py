from django.contrib import admin

from zoomate.models import (
    Animal,
    Profile,
    Adoption,
    Sale,
    Categories,
    Races,
    Vaccines,
    Match,
)


class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "gender",
        "race",
        "certificate",
    )

    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "profile_photo")


class MatchAdmin(admin.ModelAdmin):
    list_display = ("animal_a", "animal_b")


class AdoptionAdmin(admin.ModelAdmin):
    list_display = ("animal", "owner", "created_at", "modified_at")


class SaleAdmin(admin.ModelAdmin):
    list_display = ("animal", "owner", "price", "created_at", "modified_at")


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")


class RacesAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


class VaccinesAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Races, RacesAdmin)
admin.site.register(Vaccines, VaccinesAdmin)
