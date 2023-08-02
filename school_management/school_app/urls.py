from django.urls import path
from . import views
from . import api
from .api import ClassroomCreate,StudentList, UserLoginAPIView
from .api import SchoolAPI, SchoolAPIView, SchoolBranchAPI, SchoolBranchAPIView, TeacherAPI, TeacherAPIView, StudentAPI, StudentAPIView
from .api import ClassroomDetailView


urlpatterns = [
    path('admin-school/', views.admin_school_view, name='admin-school'),
    path('branch-manager-school/', views.branch_manager_school_view, name='branch-manager-school'),
    path('school-admin-branches/', views.school_admin_branches_view, name='school-admin-branches'),
    path('branch-manager-branches/', views.branch_manager_branches_view, name='branch-manager-branches'),
    path('school-branch-classrooms/<int:branch_id>/', views.school_branch_classrooms_view, name='school-branch-classrooms'),
    path('school-branches/<int:school_id>/', views.school_branches_view, name='school-branches'),
    path('teacher-grades/<int:teacher_id>/', views.teacher_grades_view, name='teacher-grades'),
    path('teacher-subjects/<int:teacher_id>/', views.teacher_subjects_view, name='teacher-subjects'),
    path('teacher-schools/<int:teacher_id>/', views.teacher_schools_view, name='teacher-schools'),
    path('teacher-classrooms/<int:teacher_id>/', views.teacher_classrooms_view, name='teacher-classrooms'),
    path('student-classroom/<int:student_id>/', views.student_classroom_view, name='student-classroom'),
    path('student-school/<int:student_id>/', views.student_school_view, name='student-school'),
    path('classroom-students/<int:classroom_id>/', views.classroom_students_view, name='classroom-students'),
    path('classroom-subjects/<int:classroom_id>/', views.classroom_subjects_view, name='classroom-subjects'),
    path('subject-teachers/<int:subject_id>/', views.subject_teachers_view, name='subject-teachers'),
    path('school-branch-teachers/<int:branch_id>/', views.school_branch_teachers_view, name='school-branch-teachers'),
    path('school-branch-students/<int:branch_id>/', views.school_branch_students_view, name='school-branch-students'),
    # APi urls
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/school/<int:school_id>/classrooms/', api.SchoolClassroomsList.as_view()),
    path('api/branch/<int:branch_id>/classrooms/', api.SchoolBranchClassroomsList.as_view()),
    path('api/classroom/new/', ClassroomCreate.as_view(), name='classroom-create'),
    path('students/', StudentList.as_view(), name='student-list'),
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



