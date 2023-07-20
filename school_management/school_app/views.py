from django.shortcuts import render
from .models import User, UserProfile, School, SchoolBranch, Classroom, Student, Teacher, Subject, ClassroomSubjectTeacher

# User is admin of which school?
def admin_school_view(request):
    admin_username = 'essaarshad'
    try:
        admin_user = User.objects.get(username=admin_username)
        try:
            admin_profile = UserProfile.objects.get(user=admin_user, role=UserProfile.SCHOOL_ADMIN)
            admin_schools = School.objects.filter(
                branches__admins=admin_profile
            )
            return render(request, 'admin_school.html', {'admin_schools': admin_schools})
        except UserProfile.DoesNotExist:
            return render(request, 'failure.html', {'message': f"No UserProfile found for admin user '{admin_username}'."})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"Admin user '{admin_username}' does not exist."})

# User is branch_manager of which school?
def branch_manager_school_view(request):
    branch_manager_username = 'branch_manager'
    try:
        branch_manager_user = User.objects.get(username=branch_manager_username)
        try:
            branch_manager_profile = UserProfile.objects.get(user=branch_manager_user, role=UserProfile.SCHOOL_BRANCH_MANAGER)
            branch_manager_schools = School.objects.filter(
                branches__branch_managers=branch_manager_profile
            )
            return render(request, 'branch_manager_school.html', {'branch_manager_schools': branch_manager_schools})
        except UserProfile.DoesNotExist:
            return render(request, 'failure.html', {'message': f"No UserProfile found for branch manager user '{branch_manager_username}'."})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"Branch manager user '{branch_manager_username}' does not exist."})

# Get all school branches a school_admin is linked to
def school_admin_branches_view(request):
    school_admin_username = 'admin'
    try:
        school_admin = User.objects.get(username=school_admin_username)
        try:
            school_admin_profile = UserProfile.objects.get(user=school_admin, role=UserProfile.SCHOOL_ADMIN)
            school_branches = SchoolBranch.objects.filter(admins=school_admin_profile)
            return render(request, 'school_admin_branches.html', {'school_branches': school_branches})
        except UserProfile.DoesNotExist:
            return render(request, 'failure.html', {'message': f"No UserProfile found for school admin user '{school_admin_username}'."})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"School admin user '{school_admin_username}' does not exist."})

# Get all school branches a branch_manager is linked to
def branch_manager_branches_view(request):
    branch_manager_username = 'branch_manager'
    try:
        branch_manager = User.objects.get(username=branch_manager_username)
        try:
            branch_manager_profile = UserProfile.objects.get(user=branch_manager, role=UserProfile.SCHOOL_BRANCH_MANAGER)
            school_branches = SchoolBranch.objects.filter(branch_managers=branch_manager_profile)
            return render(request, 'branch_manager_branches.html', {'school_branches': school_branches})
        except UserProfile.DoesNotExist:
            return render(request, 'failure.html', {'message': f"No UserProfile found for branch manager user '{branch_manager_username}'."})
    except User.DoesNotExist:
        return render(request, 'failure.html', {'message': f"Branch manager user '{branch_manager_username}' does not exist."})

# Rest of the code remains the same
...

# Get all classrooms of a school_branch
def school_branch_classrooms_view(request, branch_id):
    classrooms = Classroom.objects.filter(branch_id=branch_id)
    return render(request, 'school_branch_classrooms.html', {'classrooms': classrooms})

# Get all branches of a school
def school_branches_view(request, school_id):
    branches = SchoolBranch.objects.filter(school_id=school_id)
    return render(request, 'school_branches.html', {'branches': branches})

# What grades a teacher can teach?
def teacher_grades_view(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        classroom_ids = ClassroomSubjectTeacher.objects.filter(teacher=teacher).values_list('classroom_id', flat=True)
        grades = Classroom.objects.filter(id__in=classroom_ids).values_list('grade', flat=True).distinct()
        return render(request, 'teacher_grades.html', {'teacher': teacher, 'grades': grades})
    except Teacher.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Teacher not found.'})

# What subjects a teacher can teach?
def teacher_subjects_view(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        subjects = Subject.objects.filter(classroom_subject_teachers__teacher=teacher)
        return render(request, 'teacher_subjects.html', {'teacher': teacher, 'subjects': subjects})
    except Teacher.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Teacher not found.'})

# In which school a teacher is teaching in (Can be none as its not mandatory)
def teacher_schools_view(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        schools = School.objects.filter(branches__classrooms__classroom_subject_teachers__teacher=teacher).distinct()
        return render(request, 'teacher_schools.html', {'teacher': teacher, 'schools': schools})
    except Teacher.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Teacher not found.'})

# List of all classrooms a teacher is teaching to
def teacher_classrooms_view(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        classrooms = Classroom.objects.filter(classroom_subject_teachers__teacher=teacher)
        return render(request, 'teacher_classrooms.html', {'teacher': teacher, 'classrooms': classrooms})
    except Teacher.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Teacher not found.'})

# Which classroom student is studying in?
def student_classroom_view(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        classroom = student.classroom
        return render(request, 'student_classroom.html', {'student': student, 'classroom': classroom})
    except Student.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Student not Found'})

# In which school a student is studying in?
def student_school_view(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        school = School.objects.get(branches__classrooms=student.classroom)
        return render(request, 'student_school.html', {'student': student, 'school': school})
    except Student.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Student not found.'})

# List of all students in a classroom
def classroom_students_view(request, classroom_id):
    students = Student.objects.filter(classroom_id=classroom_id)
    return render(request, 'classroom_students.html', {'students': students})

# List of all subjects in a classroom
def classroom_subjects_view(request, classroom_id):
    subjects = Subject.objects.filter(classroom_subject_teachers__classroom_id=classroom_id)
    return render(request, 'classroom_subjects.html', {'subjects': subjects})

# List of all teachers teaching a subject
def subject_teachers_view(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        teachers = Teacher.objects.filter(classroom_subject_teachers__subject=subject)
        return render(request, 'subject_teachers.html', {'subject': subject, 'teachers': teachers})
    except Subject.DoesNotExist:
        return render(request, 'failure.html', {'message': 'Subject not found.'})

# List of all teachers of a school branch
def school_branch_teachers_view(request, branch_id):
    teachers = Teacher.objects.filter(classroom_subject_teachers__classroom__branch_id=branch_id).distinct()
    return render(request, 'school_branch_teachers.html', {'teachers': teachers})

# List of all students of a school branch
def school_branch_students_view(request, branch_id):
    students = Student.objects.filter(classroom__branch_id=branch_id)
    return render(request, 'school_branch_students.html', {'students': students})


# Seperate Code for serializers.py:

from rest_framework import generics
from .models import Classroom, School, SchoolBranch
from .serializers import ClassroomSerializer, SchoolSerializer, SchoolBranchSerializer

class ClassroomCreate(generics.CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer



class SchoolClassroomsList(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return Classroom.objects.filter(branch__school_id=school_id)

class SchoolBranchClassroomsList(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        branch_id = self.kwargs['branch_id']
        return Classroom.objects.filter(branch_id=branch_id)


   
