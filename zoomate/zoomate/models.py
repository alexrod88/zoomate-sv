from django.db import models
from django.core.validators import int_list_validator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    upp = models.CharField(null=True, blank=True, max_length=100)
    profile_photo = models.ImageField(upload_to="profile_pics")


# TODO: Maybe get these from separate store
CATEGORY_TYPES = models.TextChoices("CategoryType", "DOG CAT HAMSTER")
GENDER_TYPES = models.TextChoices("GenderType", "MALE FEMALE")


class Animal(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # TODO: Update these with new models
    category = models.CharField(choices=CATEGORY_TYPES.choices, max_length=20)
    race = models.IntegerField()
    vaccines = models.CharField(validators=[int_list_validator], max_length=30)

    gender = models.CharField(choices=GENDER_TYPES.choices, max_length=7)
    age = models.IntegerField()
    certificate = models.CharField(blank=True, max_length=40)
    father = models.OneToOneField(
        "self", null=True, on_delete=models.CASCADE, related_name="animal_father"
    )
    mother = models.OneToOneField(
        "self", null=True, on_delete=models.CASCADE, related_name="animal_mother"
    )
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


class AnimalPhoto(models.Model):
    img = models.ImageField(upload_to="animal_imgs", null=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Match(models.Model):
    animal_a = models.OneToOneField(
        Animal, on_delete=models.CASCADE, primary_key=True, related_name="animal_a"
    )
    animal_b = models.OneToOneField(
        Animal, on_delete=models.CASCADE, related_name="animal_b"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Adoption(models.Model):
    animal = models.OneToOneField(
        Animal,
        on_delete=models.CASCADE,
        related_name="Animal",
        verbose_name="Animal in adoption",
    )
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="User",
        verbose_name="User giving adoption",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Sale(models.Model):
    animal = models.OneToOneField(
        Animal,
        on_delete=models.CASCADE,
        related_name="Animal",
        verbose_name="Animal on sale",
    )
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="User",
        verbose_name="User doing sell",
    )
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Categories(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField()


class Races(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToOne(
        Categories,
        on_delete=models.CASCADE,
        related_name="Category",
        verbose_name="Category this race belongs to",
    )


class Vaccines(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToOne(
        Categories,
        on_delete=models.CASCADE,
        related_name="Category",
        verbose_name="Category this vaccine belongs to",
    )
