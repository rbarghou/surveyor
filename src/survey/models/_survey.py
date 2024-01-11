import urllib.parse
from django.conf import settings
from django.db import models
from django.urls import reverse

from survey.models._abstract_base import AbstractBase


class SurveyQuerySet(models.QuerySet):
    """Response Queryset"""


class Survey(AbstractBase):
    """Survey"""

    objects = SurveyQuerySet.as_manager()

    survey_template = models.ForeignKey(
        "SurveyTemplate", on_delete=models.CASCADE, null=False, default=None
    )
    answers = models.JSONField(blank=True, null=True)
    user_uuid = models.UUIDField(null=True, db_index=True)
    complete = models.BooleanField(default=False, null=False)

    @property
    def survey_url(self):
        """survey url"""
        if self.survey_template.site:
            protocol = settings.SITE_PROTOCOL
            domain = self.survey_template.site.domain
            path = reverse("survey-response", args=(self.id,))
            return urllib.parse.urlunparse(
                [
                    protocol,
                    domain,
                    path,
                    "",
                    "",
                    "",
                ]
            )
        return None

    def __str__(self):
        return super().__str__() + f" for {self.survey_template}"

    def save(self, update_fields=None, **kwargs):
        """save"""
        self.complete = self.answers is not None
        if update_fields and "complete" not in update_fields:
            update_fields = set(update_fields)
            update_fields.add("complete")
            update_fields = list(update_fields)
        super().save(update_fields=update_fields, **kwargs)
