from rest_framework import permissions
from school_app.models import SchoolBranch, UserProfile,Classroom
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from .models import SchoolBranch

class HasAccessOfSchoolBranch(permissions.BasePermission):
    message = "You don't have access to this school branch."

    def has_permission(self, request, view):
        classroom_id = view.kwargs['pk'] if 'pk' in view.kwargs else None

        if classroom_id is None:
            return False

        try:
            classroom = Classroom.objects.get(id=classroom_id)

            school_branch = classroom.branch

            return request.user.id in school_branch.branch_managers.values_list('id', flat=True)

        except (Classroom.DoesNotExist, SchoolBranch.DoesNotExist):
            return False

