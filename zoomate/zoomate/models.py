from django.db import models
from django.core.validators import int_list_validator

# TODO: Maybe get these from separate store
CATEGORY_TYPES = models.TextChoices('CategoryType', 'DOG CAT HAMSTER')
GENDER_TYPES = models.TextChoices('GenderType', 'MALE FEMALE')

class Parent(models.Model):
    category = models.CharField(choices=CATEGORY_TYPES.choices, max_length=30)
    gender = models.CharField(choices=GENDER_TYPES.choices, max_length=7)
    race = models.IntegerField()
    certificate = models.CharField(blank=True, max_length=30)

class Pet(models.Model):

    name = models.CharField(max_length=30)
    category = models.CharField(choices=CATEGORY_TYPES.choices, max_length=20)
    gender = models.CharField(choices=GENDER_TYPES.choices, max_length=7)
    race = models.IntegerField()
    age = models.IntegerField()
    certificate = models.CharField(blank=True, max_length=30)
    vaccines = models.CharField(validators=[int_list_validator], max_length=30)
    father = models.OneToOneField(Parent, on_delete=models.CASCADE,
                                  verbose_name="pet's father",
                                  related_name='father')
    # TODO: Add photos Model (list of string)

class Adoption(models.Model):
    animal = models.OneToOneField(
        Animal, on_delete=models.CASCADE, related_name='Animal', verbose_name='Animal in adoption')
    owner = models.OneToOneField(User, on_delete=models.CASCADE,
                                 related_name='User', verbose_name="User giving adoption")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Sale(models.Model):
    animal = models.OneToOneField(
        Animal, on_delete=models.CASCADE, related_name='Animal', verbose_name='Animal on sale')
    owner = models.OneToOneField(User, on_delete=models.CASCADE,
                                 related_name='User', verbose_name="User doing sell")
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Categories(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField()


class Races(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToOne(Categories, on_delete=models.CASCADE,
                                related_name='Category', verbose_name='Category this race belongs to')


class Vaccines(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToOne(Categories, on_delete=models.CASCADE,
                                related_name='Category', verbose_name='Category this vaccine belongs to')
