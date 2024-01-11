from django.db import models

from survey.models._abstract_base import AbstractBase


class SurveyTemplateQuerySet(models.QuerySet):
    """SurveyTemplate QuerySet"""


class SurveyTemplate(AbstractBase):
    """SurveyTemplate"""

    objects = SurveyTemplateQuerySet.as_manager()

    site = models.ForeignKey("sites.Site", on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    json = models.JSONField(blank=False, null=False)

    def __str__(self):
        return f"SurveyTemplate: {self.name}"
