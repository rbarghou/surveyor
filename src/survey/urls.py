"""surveyor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_social_oauth2.authentication import SocialAuthentication

from survey.permissions import SurveyPermission, SurveyTemplatePermission
from survey.views import SurveyView
from survey.viewsets import SurveyViewSet, SurveyTemplateViewSet

router = DefaultRouter()
router.register(r"surveys", SurveyViewSet)
router.register(r"survey_templates", SurveyTemplateViewSet)


schema_view = get_schema_view(
    title="surveyor",
    patterns=router.urls,
    public=False,
    permission_classes=(SurveyPermission, SurveyTemplatePermission),
    authentication_classes=[SocialAuthentication],
)

urlpatterns = [
    path("s/<uuid:pk>", SurveyView.as_view(), name="survey-response"),
    path("openapi", schema_view, name="openapi-schema"),
] + router.urls
