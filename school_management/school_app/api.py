from rest_framework import generics
from .models import Classroom, School, SchoolBranch
from .serializers import ClassroomSerializer
from .models import Student
from .serializers import StudentSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework import generics, pagination, authentication,permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import UserProfile

class IsSchoolAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == UserProfile.SCHOOL_ADMIN

class ClassroomCreate(generics.CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

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


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)



from .serializers import SchoolSerializer, SchoolBranchSerializer, TeacherSerializer
from .models import Teacher

# For School
class SchoolAPI(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

class SchoolDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

# For School Branch
class SchoolBranchAPI(generics.ListCreateAPIView):
    queryset = SchoolBranch.objects.all()
    serializer_class = SchoolBranchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

class SchoolBranchDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolBranch.objects.all()
    serializer_class = SchoolBranchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

# For Teacher
class TeacherAPI(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

class TeacherDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

# For Student
class StudentAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]
