# Generated by Django 4.2.6 on 2023-10-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0003_alter_personal_tipo_documento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventarios",
            name="fecha_creacion",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="tipo_documento",
            field=models.CharField(
                choices=[
                    ("DNI", "Documento N. Identidad"),
                    ("CNT", "Carnet de Extranjeria"),
                ],
                default="DNI",
                max_length=3,
            ),
        ),
    ]
