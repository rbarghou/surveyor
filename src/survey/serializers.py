from rest_framework.serializers import ModelSerializer, ReadOnlyField

from survey.models import Survey, SurveyTemplate


class SurveySerializer(ModelSerializer):
    """SurveySerializer"""

    survey_url = ReadOnlyField()

    class Meta:
        model = Survey
        fields = "__all__"


class SurveyTemplateSerializer(ModelSerializer):
    """SurveyTemplateSerializer"""

    class Meta:
        model = SurveyTemplate
        fields = "__all__"
