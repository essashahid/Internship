from django.urls import path
from . import views
from . import api

from .api import (
    ClassroomCreate, UserLoginAPIView,
    SchoolAPI, SchoolAPIView, SchoolBranchAPI, SchoolBranchAPIView,
    TeacherAPI, TeacherAPIView, StudentAPI, StudentAPIView,
    ClassroomDetailView,SchoolBranchClassroomsList,SchoolClassroomsList
)

from .views import (
    AdminSchoolView, BranchManagerSchoolView, SchoolAdminBranchesView, BranchManagerBranchesView,
    SchoolBranchClassroomsView, SchoolBranchesView, TeacherGradesView, TeacherSubjectsView,
    TeacherSchoolsView, TeacherClassroomsView, StudentClassroomView, StudentSchoolView,
    ClassroomStudentsView, ClassroomSubjectsView, SubjectTeachersView, SchoolBranchTeachersView,
    SchoolBranchStudentsView
)

regular_view_patterns = [
    path('admin-school/', AdminSchoolView.as_view(), name='admin-school'),
    path('branch-manager-school/', BranchManagerSchoolView.as_view(), name='branch-manager-school'),
    path('school-admin-branches/', SchoolAdminBranchesView.as_view(), name='school-admin-branches'),
    path('branch-manager-branches/', BranchManagerBranchesView.as_view(), name='branch-manager-branches'),
    path('school-branch-classrooms/<int:branch_id>/', SchoolBranchClassroomsView.as_view(), name='school-branch-classrooms'),
    path('school-branches/<int:school_id>/', SchoolBranchesView.as_view(), name='school-branches'),
    path('teacher-grades/<int:teacher_id>/', TeacherGradesView.as_view(), name='teacher-grades'),
    path('teacher-subjects/<int:teacher_id>/', TeacherSubjectsView.as_view(), name='teacher-subjects'),
    path('teacher-schools/<int:teacher_id>/', TeacherSchoolsView.as_view(), name='teacher-schools'),
    path('teacher-classrooms/<int:teacher_id>/', TeacherClassroomsView.as_view(), name='teacher-classrooms'),
    path('student-classroom/<int:student_id>/', StudentClassroomView.as_view(), name='student-classroom'),
    path('student-school/<int:student_id>/', StudentSchoolView.as_view(), name='student-school'),
    path('classroom-students/<int:classroom_id>/', ClassroomStudentsView.as_view(), name='classroom-students'),
    path('classroom-subjects/<int:classroom_id>/', ClassroomSubjectsView.as_view(), name='classroom-subjects'),
    path('subject-teachers/<int:subject_id>/', SubjectTeachersView.as_view(), name='subject-teachers'),
    path('school-branch-teachers/<int:branch_id>/', SchoolBranchTeachersView.as_view(), name='school-branch-teachers'),
    path('school-branch-students/<int:branch_id>/', SchoolBranchStudentsView.as_view(), name='school-branch-students'),
]

api_view_patterns = [
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/school/<int:school_id>/classrooms/', SchoolClassroomsList.as_view()),
    path('api/branch/<int:branch_id>/classrooms/', SchoolBranchClassroomsList.as_view()),
    path('api/classroom/new/', ClassroomCreate.as_view(), name='classroom-create'),
    path('api/school/', SchoolAPI.as_view(), name='school_api'),
    path('api/school/<int:pk>/', SchoolAPIView.as_view(), name='school_detail_api'),
    path('api/school-branch/', SchoolBranchAPI.as_view(), name='school_branch_api'),
    path('api/school-branch/<int:pk>/', SchoolBranchAPIView.as_view(), name='school_branch_detail_api'),
    path('api/teacher/', TeacherAPI.as_view(), name='teacher_api'),
    path('api/teacher/<int:pk>/', TeacherAPIView.as_view(), name='teacher_detail_api'),
    path('api/student/', StudentAPI.as_view(), name='student_api'),
    path('api/student/<int:pk>/', StudentAPIView.as_view(), name='student_detail_api'),
    path('classrooms/<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
]

urlpatterns = regular_view_patterns + api_view_patterns



