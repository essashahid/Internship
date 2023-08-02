from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import User, UserProfile, School, SchoolBranch, Classroom, Student, Teacher, Subject, ClassroomSubjectTeacher

def get_user_profile(username, role):
    try:
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user, role=role)
        return profile
    except User.DoesNotExist:
        raise ObjectDoesNotExist(f"User '{username}' does not exist.")
    except UserProfile.DoesNotExist:
        raise ObjectDoesNotExist(f"No UserProfile found for user '{username}'.")

def handle_object_not_found(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except ObjectDoesNotExist as e:
            return render(request, 'failure.html', {'message': str(e)})
    return wrapper

@handle_object_not_found
def admin_school_view(request):
    admin_username = 'essaarshad'
    admin_profile = get_user_profile(admin_username, UserProfile.SCHOOL_ADMIN)
    admin_schools = School.objects.filter(branches__admins=admin_profile)
    return render(request, 'admin_school.html', {'admin_schools': admin_schools})

@handle_object_not_found
def branch_manager_school_view(request):
    branch_manager_username = 'branch_manager'
    branch_manager_profile = get_user_profile(branch_manager_username, UserProfile.SCHOOL_BRANCH_MANAGER)
    branch_manager_schools = School.objects.filter(branches__branch_managers=branch_manager_profile)
    return render(request, 'branch_manager_school.html', {'branch_manager_schools': branch_manager_schools})

@handle_object_not_found
def school_admin_branches_view(request):
    school_admin_username = 'admin'
    school_admin_profile = get_user_profile(school_admin_username, UserProfile.SCHOOL_ADMIN)
    school_branches = SchoolBranch.objects.filter(admins=school_admin_profile)
    return render(request, 'school_admin_branches.html', {'school_branches': school_branches})

@handle_object_not_found
def branch_manager_branches_view(request):
    branch_manager_username = 'branch_manager'
    branch_manager_profile = get_user_profile(branch_manager_username, UserProfile.SCHOOL_BRANCH_MANAGER)
    school_branches = SchoolBranch.objects.filter(branch_managers=branch_manager_profile)
    return render(request, 'branch_manager_branches.html', {'school_branches': school_branches})

def school_branch_classrooms_view(request, branch_id):
    classrooms = Classroom.objects.filter(branch_id=branch_id)
    return render(request, 'school_branch_classrooms.html', {'classrooms': classrooms})

def school_branches_view(request, school_id):
    branches = SchoolBranch.objects.filter(school_id=school_id)
    return render(request, 'school_branches.html', {'branches': branches})

@handle_object_not_found
def teacher_grades_view(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    classroom_ids = ClassroomSubjectTeacher.objects.filter(teacher=teacher).values_list('classroom_id', flat=True)
    grades = Classroom.objects.filter(id__in=classroom_ids).values_list('grade', flat=True).distinct()
    return render(request, 'teacher_grades.html', {'teacher': teacher, 'grades': grades})

@handle_object_not_found
def teacher_subjects_view(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    subjects = Subject.objects.filter(classroom_subject_teachers__teacher=teacher)
    return render(request, 'teacher_subjects.html', {'teacher': teacher, 'subjects': subjects})

@handle_object_not_found
def teacher_schools_view(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    schools = School.objects.filter(branches__classrooms__classroom_subject_teachers__teacher=teacher).distinct()
    return render(request, 'teacher_schools.html', {'teacher': teacher, 'schools': schools})

@handle_object_not_found
def teacher_classrooms_view(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    classrooms = Classroom.objects.filter(classroom_subject_teachers__teacher=teacher)
    return render(request, 'teacher_classrooms.html', {'teacher': teacher, 'classrooms': classrooms})

@handle_object_not_found
def student_classroom_view(request, student_id):
    student = Student.objects.get(id=student_id)
    classroom = student.classroom
    return render(request, 'student_classroom.html', {'student': student, 'classroom': classroom})

@handle_object_not_found
def student_school_view(request, student_id):
    student = Student.objects.get(id=student_id)
    school = School.objects.get(branches__classrooms=student.classroom)
    return render(request, 'student_school.html', {'student': student, 'school': school})

def classroom_students_view(request, classroom_id):
    students = Student.objects.filter(classroom_id=classroom_id)
    return render(request, 'classroom_students.html', {'students': students})

def classroom_subjects_view(request, classroom_id):
    subjects = Subject.objects.filter(classroom_subject_teachers__classroom_id=classroom_id)
    return render(request, 'classroom_subjects.html', {'subjects': subjects})

@handle_object_not_found
def subject_teachers_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    teachers = Teacher.objects.filter(classroom_subject_teachers__subject=subject)
    return render(request, 'subject_teachers.html', {'subject': subject, 'teachers': teachers})

def school_branch_teachers_view(request, branch_id):
    teachers = Teacher.objects.filter(classroom_subject_teachers__classroom__branch_id=branch_id).distinct()
    return render(request, 'school_branch_teachers.html', {'teachers': teachers})

def school_branch_students_view(request, branch_id):
    students = Student.objects.filter(classroom__branch_id=branch_id)
    return render(request, 'school_branch_students.html', {'students': students})
