from django.contrib import admin

from zoomate.models import Animal, Profile

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender', 'race', 'certificate',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo')

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Profile, ProfileAdmin)
