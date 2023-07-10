from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User, School, SchoolBranch, Classroom, Student, Teacher, Subject, ClassroomSubjectTeacher

def admin_school_view(request):
    admin_username = 'admin'
    try:
        admin_school = User.objects.get(username=admin_username).school
        return render(request, 'admin_school.html', {'admin_school': admin_school})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"Admin user '{admin_username}' does not exist."})

def branch_manager_school_view(request):
    branch_manager_username = 'branch_manager'
    try:
        branch_manager_school = User.objects.get(username=branch_manager_username).schoolbranch.school
        return render(request, 'branch_manager_school.html', {'branch_manager_school': branch_manager_school})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"Branch manager user '{branch_manager_username}' does not exist."})

def school_admin_branches_view(request):
    school_admin_username = 'admin'
    try:
        school_admin = User.objects.get(username=school_admin_username)
        school_branches = SchoolBranch.objects.filter(school=school_admin.school)
        return render(request, 'school_admin_branches.html', {'school_branches': school_branches})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"School admin user '{school_admin_username}' does not exist."})

def branch_manager_branches_view(request):
    branch_manager_username = 'branch_manager'
    try:
        branch_manager = User.objects.get(username=branch_manager_username)
        school_branches = SchoolBranch.objects.filter(branch_manager=branch_manager)
        return render(request, 'branch_manager_branches.html', {'school_branches': school_branches})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"Branch manager user '{branch_manager_username}' does not exist."})

def school_branch_classrooms_view(request, branch_id):
    classrooms = Classroom.objects.filter(branch_id=branch_id)
    return render(request, 'school_branch_classrooms.html', {'classrooms': classrooms})

def school_branches_view(request, school_id):
    branches = SchoolBranch.objects.filter(school_id=school_id)
    return render(request, 'school_branches.html', {'branches': branches})

def teacher_grades_view(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        classroom_ids = ClassroomSubjectTeacher.objects.filter(teacher=teacher).values_list('classroom_id', flat=True)
        grades = Classroom.objects.filter(id__in=classroom_ids).values_list('grade', flat=True).distinct()
        return render(request, 'teacher_grades.html', {'teacher': teacher, 'grades': grades})
    except Teacher.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Teacher not found.'})



# Implement the remaining views for the other queries


