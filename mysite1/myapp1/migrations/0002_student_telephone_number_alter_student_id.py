# Generated by Django 4.2.5 on 2023-09-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="telephone_number",
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
