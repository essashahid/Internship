from rest_framework import generics, pagination, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from .models import Classroom, School, SchoolBranch, Student, UserProfile, Teacher
from .serializers import ClassroomSerializer, StudentSerializer, SchoolSerializer, SchoolBranchSerializer, TeacherSerializer
from .permissions import IsRelatedToClassroom


class IsSchoolAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == UserProfile.SCHOOL_ADMIN


class ClassroomCreate(generics.CreateAPIView):
    serializer_class = ClassroomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]


class SchoolClassroomsList(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        school_id = self.kwargs['branch_id']
        return Classroom.objects.filter(branch__school_id=school_id)


class SchoolBranchClassroomsList(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        branch_id = self.kwargs['branch_id']
        return School.objects.filter(branch_id=branch_id)


class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        school_id = self.kwargs['branch_id']
        return Student.objects.filter(branch__school_id=school_id)


class SchoolAPI(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        return School.objects.all()


class SchoolDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return School.objects.filter(id=school_id)


class SchoolBranchAPI(generics.ListCreateAPIView):
    serializer_class = SchoolBranchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return SchoolBranch.objects.filter(school_id=school_id)


class SchoolBranchDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolBranchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return SchoolBranch.objects.filter(school_id=school_id)


class TeacherAPI(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return Teacher.objects.filter(branch__school_id=school_id)


class TeacherDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return Teacher.objects.filter(branch__school_id=school_id)


class StudentAPI(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return Student.objects.filter(classroom__branch__school_id=school_id)


class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['school_id']
        return Student.objects.filter(classroom__branch__school_id=school_id)


class ClassroomDetailView(generics.RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsRelatedToClassroom]

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj



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


# For School
class SchoolAPI(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['branch_id']
        return School.objects.filter(branch__school_id=school_id)

class SchoolDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # queryset = School.objects.all()
    serializer_class = SchoolSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['pk']
        return School.objects.filter(pk=school_id)


# For School Branch
class SchoolBranchAPI(generics.ListCreateAPIView):
    serializer_class = SchoolBranchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['branch_id']
        return SchoolBranch.objects.filter(branch__school_id=school_id)

class SchoolBranchDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolBranchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['pk']
        return SchoolBranch.objects.filter(pk=school_id)


# For Teacher
class TeacherAPI(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]


    def get_queryset(self):
        school_id = self.kwargs['branch_id']
        return Teacher.objects.filter(branch__school_id=school_id)

class TeacherDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]


    def get_queryset(self):
        school_id = self.kwargs['pk']
        return Teacher.objects.filter(pk=school_id)



class StudentAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['pk']
        return Student.objects.filter(pk=school_id)



class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

    def get_queryset(self):
        school_id = self.kwargs['pk']
        return S.objects.filter(pk=school_id)



class ClassroomDetailView(generics.RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsRelatedToClassroom]

    def get_queryset(self):
        school_id = self.kwargs['branch_id']
        return Classroom.objects.filter(branch__school_id=school_id)


    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj




