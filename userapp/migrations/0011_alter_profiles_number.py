# Generated by Django 5.0.1 on 2024-01-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userapp", "0010_alter_profiles_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profiles",
            name="number",
            field=models.CharField(max_length=12),
        ),
    ]
