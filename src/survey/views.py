import json

from django.forms import Form, Field
from django.http.response import JsonResponse
from django.views.generic import UpdateView

from survey.models import Survey


class SurveyForm(Form):
    """SurveyForm"""

    answers = Field(required=True)


class SurveyView(UpdateView):
    """SurveyView"""

    template_name = "survey.html"
    model = Survey
    form_class = SurveyForm

    def get_form(self):
        """get_form: specify data load"""
        if self.request.body:
            data = json.loads(self.request.body.decode())
            return SurveyForm(data)
        return SurveyForm()

    def form_valid(self, form):
        """Save answers from form."""
        self.object.answers = form.data["answers"]
        self.object.save()
        return JsonResponse({"status": "complete"})

    def form_invalid(self, form):
        """Respond with incomplete"""
        return JsonResponse({"status": "incomplete"})
