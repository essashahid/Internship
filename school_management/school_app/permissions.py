from rest_framework import permissions
from school_app.models.user_profile import UserProfile


class IsRelatedToClassroom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        user_profile = request.user.profile

        is_teacher = obj.classroom_subject_teachers.filter(teacher__name=user_profile.user.username).exists()
        is_student = obj.students.filter(name=user_profile.user.username).exists()

        is_school_admin = (user_profile.role == UserProfile.SCHOOL_ADMIN or user_profile.admin_school_branches.filter(school=obj.branch.school).exists())
        is_branch_manager = (user_profile.role == UserProfile.SCHOOL_BRANCH_MANAGER or user_profile.manager_school_branches.filter(id=obj.branch.id).exists())


        return is_teacher or is_student or is_school_admin or is_branch_manager
