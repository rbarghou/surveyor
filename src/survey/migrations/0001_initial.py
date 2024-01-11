# Generated by Django 3.2.23 on 2024-01-11 15:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="SurveyTemplate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=128, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("json", models.JSONField()),
                (
                    "site",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="sites.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Survey",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("answers", models.JSONField(blank=True, null=True)),
                ("user_uuid", models.UUIDField(db_index=True, null=True)),
                ("complete", models.BooleanField(default=False)),
                (
                    "survey_template",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.surveytemplate",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
