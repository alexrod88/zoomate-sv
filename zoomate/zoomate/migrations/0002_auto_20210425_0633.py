# Generated by Django 3.1.4 on 2021-04-25 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("zoomate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="img",
            field=models.ImageField(null=True, upload_to="animal_imgs"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="zoomate.categories"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="race",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="zoomate.races"
            ),
        ),
        migrations.RemoveField(
            model_name="animal",
            name="vaccines",
        ),
        migrations.AddField(
            model_name="animal",
            name="vaccines",
            field=models.ManyToManyField(to="zoomate.Vaccines"),
        ),
        migrations.DeleteModel(
            name="AnimalPhoto",
        ),
    ]
