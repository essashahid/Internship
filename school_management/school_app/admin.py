from django.contrib import admin
from .models import User, UserProfile, School, SchoolBranch, Classroom, Student, Teacher, Subject, ClassroomSubjectTeacher


# Register your models here.


admin.site.register(School)

# admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(School)
admin.site.register(SchoolBranch)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(ClassroomSubjectTeacher)


