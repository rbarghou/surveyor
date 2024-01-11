import uuid

import pytest

from survey.models import Survey, SurveyTemplate


@pytest.mark.django_db
def test_survey_save():
    """Test Survey Save"""
    survey_template = SurveyTemplate.objects.create(
        name="Test Survey Tempalte", json={"key": "value"}
    )
    survey = Survey.objects.create(
        survey_template=survey_template, user_uuid=uuid.uuid4()
    )
    survey.save()

    assert not survey.complete

    survey.answers = {"key": "value"}
    survey.save()

    assert survey.complete
