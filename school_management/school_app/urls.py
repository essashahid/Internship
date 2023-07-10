from django.urls import path
from . import views
urlpatterns = [
    path('admin-school/', views.admin_school_view, name='admin-school'),
    path('branch-manager-school/', views.branch_manager_school_view, name='branch-manager-school'),
    path('school-admin-branches/', views.school_admin_branches_view, name='school-admin-branches'),
    path('branch-manager-branches/', views.branch_manager_branches_view, name='branch-manager-branches'),
    path('school-branch-classrooms/<int:branch_id>/', views.school_branch_classrooms_view, name='school-branch-classrooms'),
    path('school-branches/<int:school_id>/', views.school_branches_view, name='school-branches'),
    path('teacher-grades/<int:teacher_id>/', views.teacher_grades_view, name='teacher-grades'),


    
    # Add more URL patterns for other views
]
