from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import SAFE_METHODS
from rest_framework.schemas.openapi import AutoSchema as _AutoSchema
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from survey.models import Survey, SurveyTemplate
from survey.permissions import SurveyPermission, SurveyTemplatePermission
from survey.serializers import SurveySerializer, SurveyTemplateSerializer


class AutoSchema(_AutoSchema):
    """Custom AutoSchema to include authentication"""

    def get_operation(self, path, method):
        """get_operation performs standard open_api.AutoSchema.get_operation but adds security
        to appropriate opperation.  This is analogous to drf-yasg's approach but much lighter
        weight than using the whole drf-yasg.

        For more information: https://www.django-rest-framework.org/api-guide/schemas/#autoschema

        NOTE: This documents the use of AutoSchema on an APIView, but not on a ViewSet.  However,
        this is nearly identical, except for the schema.get_operation being called once per
        view generated with the `ViewSet.as_view()` on each action
        """
        operation = super().get_operation(path, method)

        resource = self.view.resource
        action = "read" if method in SAFE_METHODS else "write"
        operation["security"] = [{"auth-server": [f"surveyor:{resource}:{action}:"]}]
        return operation


class SurveyViewSet(ModelViewSet):
    """SurveyViewSet"""

    schema = AutoSchema()
    serializer_class = SurveySerializer
    permission_classes = [(IsAuthenticated & SurveyPermission) | IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["created"]
    queryset = Survey.objects.all()
    resource = "surveys"
    filterset_fields = ["survey_template", "user_uuid", "complete"]


class SurveyTemplateViewSet(ModelViewSet):
    """SurveyTemplateViewSet"""

    schema = AutoSchema()
    serializer_class = SurveyTemplateSerializer
    permission_classes = [(IsAuthenticated & SurveyTemplatePermission) | IsAdminUser]
    queryset = SurveyTemplate.objects.all()
    resource = "survey_templates"
