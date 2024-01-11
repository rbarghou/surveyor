from django.core.cache import cache
from rest_framework.permissions import BasePermission, SAFE_METHODS


class SurveyorBasePermission(BasePermission):
    """SurveyorBasePermission"""

    scopes = {}

    @staticmethod
    def get_user_scopes(token):
        """Get User Scopes"""
        cached_user_auth_data = cache.get(token)
        if not cached_user_auth_data:
            return []
        user_scopes = cached_user_auth_data.get("scope", [])
        return user_scopes

    def has_permission(self, request, view):
        """
        Grants access if the user is staff, or has the proper read/write scopes
        """
        scope_type = "read" if request.method in SAFE_METHODS else "write"

        if scope_type not in self.scopes or not self.scopes[scope_type]:
            return False

        user_scopes = self.get_user_scopes(request.auth)
        return self.scopes[scope_type] and self.scopes[scope_type] in user_scopes


class SurveyTemplatePermission(SurveyorBasePermission):
    """SurveyTemplatePermissions"""

    scopes = {
        scope_type: f"surveyor:survey_templates:{scope_type}"
        for scope_type in ("read", "write")
    }


class SurveyPermission(SurveyorBasePermission):
    """SurveyPermission"""

    scopes = {
        scope_type: f"surveyor:surveys:{scope_type}" for scope_type in ("read", "write")
    }
