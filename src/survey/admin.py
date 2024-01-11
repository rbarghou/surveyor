from django.contrib import admin
from django.utils.html import format_html

from survey.models import Survey, SurveyTemplate


@admin.register(SurveyTemplate)
class SurveyTemplateAdmin(admin.ModelAdmin):
    """SurveyTemplateAdmin"""

    readonly_fields = ("created", "modified")


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """SurveyAdmin"""

    readonly_fields = ("link", "created", "modified")

    @staticmethod
    def link(obj):
        """Link"""
        _url = obj.survey_url
        if _url:
            return format_html('<a href="{_url}">{_url}</a>', _url=_url)
        return format_html("<span>No Link</span>")

    link.short_description = "link"
