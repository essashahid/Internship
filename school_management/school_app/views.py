from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import User, UserProfile, School, SchoolBranch, Classroom, Student, Teacher, Subject, ClassroomSubjectTeacher
from django.views import View

def get_user_by_username_and_role(username, role):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user, role=role)
    return profile

def handle_object_not_found(view_class):
    class WrappedView(view_class):
        def dispatch(self, request, *args, **kwargs):
            try:
                return super().dispatch(request, *args, **kwargs)
            except ObjectDoesNotExist as e:
                return render(request, 'failure.html', {'message': str(e)})
    return WrappedView

class AdminSchoolView(View):
    template_name = 'admin_school.html'
    def get(self, request):
        admin_username = 'essaarshad'
        admin_profile = get_user_by_username_and_role(admin_username, UserProfile.SCHOOL_ADMIN)
        admin_schools = School.objects.filter(branches__admins=admin_profile)
        return render(request, self.template_name, {'admin_schools': admin_schools})

class BranchManagerSchoolView(View):
    template_name = 'branch_manager_school.html'
    def get(self, request):
        branch_manager_username = 'branch_manager'
        branch_manager_profile = get_user_by_username_and_role(branch_manager_username, UserProfile.SCHOOL_BRANCH_MANAGER)
        branch_manager_schools = School.objects.filter(branches__branch_managers=branch_manager_profile)
        return render(request, self.template_name, {'branch_manager_schools': branch_manager_schools})

class SchoolAdminBranchesView(View):
    template_name = 'school_admin_branches.html'
    def get(self, request):
        school_admin_username = 'admin'
        school_admin_profile = get_user_by_username_and_role(school_admin_username, UserProfile.SCHOOL_ADMIN)
        school_branches = SchoolBranch.objects.filter(admins=school_admin_profile)
        return render(request, self.template_name, {'school_branches': school_branches})

class BranchManagerBranchesView(View):
    template_name = 'branch_manager_branches.html'
    def get(self, request):
        branch_manager_username = 'branch_manager'
        branch_manager_profile = get_user_by_username_and_role(branch_manager_username, UserProfile.SCHOOL_BRANCH_MANAGER)
        school_branches = SchoolBranch.objects.filter(branch_managers=branch_manager_profile)
        return render(request, self.template_name, {'school_branches': school_branches})

class SchoolBranchClassroomsView(View):
    template_name = 'school_branch_classrooms.html'
    def get(self, request, branch_id):
        classrooms = Classroom.objects.filter(branch_id=branch_id)
        return render(request, self.template_name, {'classrooms': classrooms})

class SchoolBranchesView(View):
    template_name = 'school_branches.html'
    def get(self, request, school_id):
        branches = SchoolBranch.objects.filter(school_id=school_id)
        return render(request, self.template_name, {'branches': branches})

class TeacherGradesView(View):
    template_name = 'teacher_grades.html'
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        classroom_ids = ClassroomSubjectTeacher.objects.filter(teacher=teacher).values_list('classroom_id', flat=True)
        grades = Classroom.objects.filter(id__in=classroom_ids).values_list('grade', flat=True).distinct()
        return render(request, self.template_name, {'teacher': teacher, 'grades': grades})

class TeacherSubjectsView(View):
    template_name = 'teacher_subjects.html'
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        subjects = Subject.objects.filter(classroom_subject_teachers__teacher=teacher)
        return render(request, self.template_name, {'teacher': teacher, 'subjects': subjects})

class TeacherSchoolsView(View):
    template_name = 'teacher_schools.html'
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        schools = School.objects.filter(branches__classrooms__classroom_subject_teachers__teacher=teacher).distinct()
        return render(request, self.template_name, {'teacher': teacher, 'schools': schools})

class TeacherClassroomsView(View):
    template_name = 'teacher_classrooms.html'
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        classrooms = Classroom.objects.filter(classroom_subject_teachers__teacher=teacher)
        return render(request, self.template_name, {'teacher': teacher, 'classrooms': classrooms})

class StudentClassroomView(View):
    template_name = 'student_classroom.html'
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        classroom = student.classroom
        return render(request, self.template_name, {'student': student, 'classroom': classroom})

class StudentSchoolView(View):
    template_name = 'student_school.html'
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        school = School.objects.get(branches__classrooms=student.classroom)
        return render(request, self.template_name, {'student': student, 'school': school})

class ClassroomStudentsView(View):
    template_name = 'classroom_students.html'
    def get(self, request, classroom_id):
        students = Student.objects.filter(classroom_id=classroom_id)
        return render(request, self.template_name, {'students': students})

class ClassroomSubjectsView(View):
    template_name = 'classroom_subjects.html'
    def get(self, request, classroom_id):
        subjects = Subject.objects.filter(classroom_subject_teachers__classroom_id=classroom_id)
        return render(request, self.template_name, {'subjects': subjects})

class SubjectTeachersView(View):
    template_name = 'subject_teachers.html'
    def get(self, request, subject_id):
        subject = Subject.objects.get(id=subject_id)
        teachers = Teacher.objects.filter(classroom_subject_teachers__subject=subject)
        return render(request, self.template_name, {'subject': subject, 'teachers': teachers})

class SchoolBranchTeachersView(View):
    template_name = 'school_branch_teachers.html'
    def get(self, request, branch_id):
        teachers = Teacher.objects.filter(classroom_subject_teachers__classroom__branch_id=branch_id).distinct()
        return render(request, self.template_name, {'teachers': teachers})

class SchoolBranchStudentsView(View):
    template_name = 'school_branch_students.html'
    def get(self, request, branch_id):
        students = Student.objects.filter(classroom__branch_id=branch_id)
        return render(request, self.template_name, {'students': students})


AdminSchoolView = handle_object_not_found(AdminSchoolView)
BranchManagerSchoolView = handle_object_not_found(BranchManagerSchoolView)
SchoolAdminBranchesView = handle_object_not_found(SchoolAdminBranchesView)
BranchManagerBranchesView = handle_object_not_found(BranchManagerBranchesView)
SchoolBranchClassroomsView = handle_object_not_found(SchoolBranchClassroomsView)
SchoolBranchesView = handle_object_not_found(SchoolBranchesView)
TeacherGradesView = handle_object_not_found(TeacherGradesView)
TeacherSubjectsView = handle_object_not_found(TeacherSubjectsView)
TeacherSchoolsView = handle_object_not_found(TeacherSchoolsView)
TeacherClassroomsView = handle_object_not_found(TeacherClassroomsView)
StudentClassroomView = handle_object_not_found(StudentClassroomView)
StudentSchoolView = handle_object_not_found(StudentSchoolView)
ClassroomStudentsView = handle_object_not_found(ClassroomStudentsView)
ClassroomSubjectsView = handle_object_not_found(ClassroomSubjectsView)
SubjectTeachersView = handle_object_not_found(SubjectTeachersView)
SchoolBranchTeachersView = handle_object_not_found(SchoolBranchTeachersView)
SchoolBranchStudentsView = handle_object_not_found(SchoolBranchStudentsView)
