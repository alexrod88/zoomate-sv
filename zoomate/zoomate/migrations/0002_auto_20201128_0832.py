# Generated by Django 3.1.3 on 2020-11-28 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoomate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='father',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='animal_father', to='zoomate.animal'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='mother',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='animal_mother', to='zoomate.animal'),
        ),
    ]
