# Generated by Django 3.1.4 on 2021-01-13 20:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat'), ('HAMSTER', 'Hamster')], max_length=20)),
                ('race', models.IntegerField()),
                ('vaccines', models.CharField(max_length=30, validators=[django.core.validators.int_list_validator])),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=7)),
                ('age', models.IntegerField()),
                ('certificate', models.CharField(blank=True, max_length=40)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('father', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_father', to='zoomate.animal')),
                ('mother', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_mother', to='zoomate.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_category', to='zoomate.categories', verbose_name='Category this vaccine belongs to')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sale_animal', to='zoomate.animal', verbose_name='Animal on sale')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sale_owner', to=settings.AUTH_USER_MODEL, verbose_name='User doing sell')),
            ],
        ),
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='race_category', to='zoomate.categories', verbose_name='Category this race belongs to')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('upp', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_photo', models.ImageField(upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='animal_imgs')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomate.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomate.profile'),
        ),
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adopted_animal', to='zoomate.animal', verbose_name='Animal in adoption')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adoption_owner', to=settings.AUTH_USER_MODEL, verbose_name='User giving adoption')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('animal_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='animal_a', serialize=False, to='zoomate.animal')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('animal_b', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='animal_b', to='zoomate.animal')),
            ],
        ),
    ]
