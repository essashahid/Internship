from rest_framework import generics
from .models import Classroom, School, SchoolBranch
from .serializers import ClassroomSerializer
from .models import Student
from .serializers import StudentSerializer

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


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

