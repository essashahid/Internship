from rest_framework import generics, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from .models import Classroom, School, SchoolBranch, Student, UserProfile, Teacher
from .serializers import ClassroomSerializer, StudentSerializer, SchoolSerializer, SchoolBranchSerializer, TeacherSerializer
from .permissions import HasAccessOfSchoolBranch
from django.shortcuts import get_object_or_404

class IsSchoolAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == UserProfile.SCHOOL_ADMIN

class SchoolAdminPermissionMixin:
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsSchoolAdmin]

class ClassroomCreate(SchoolAdminPermissionMixin, generics.CreateAPIView):
    serializer_class = ClassroomSerializer

class SchoolClassroomsList(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        return Classroom.objects.filter(branch__school_id=self.kwargs['school_id'])


class SchoolBranchClassroomsList(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        return Classroom.objects.filter(branch_id=self.kwargs['branch_id'])

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Both username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)


class SchoolAdminAPIView(SchoolAdminPermissionMixin, generics.ListCreateAPIView):
    def get_queryset(self):
        return self.model_class.objects.filter(pk=self.kwargs['pk'])


class SchoolAdminDetailAPIView(SchoolAdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return self.model_class.objects.filter(pk=self.kwargs['pk'])


class SchoolAPI(SchoolAdminAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    model_class = School

class SchoolAPIView(SchoolAdminDetailAPIView):
    serializer_class = SchoolSerializer
    model_class = School

class SchoolBranchAPI(SchoolAdminAPIView):
    serializer_class = SchoolBranchSerializer
    model_class = SchoolBranch

class SchoolBranchAPIView(SchoolAdminDetailAPIView):
    serializer_class = SchoolBranchSerializer
    model_class = SchoolBranch

class TeacherAPI(SchoolAdminAPIView):
    serializer_class = TeacherSerializer
    model_class = Teacher

class TeacherAPIView(SchoolAdminDetailAPIView):
    serializer_class = TeacherSerializer
    model_class = Teacher

class StudentAPI(SchoolAdminAPIView):
    serializer_class = StudentSerializer
    model_class = Student

class StudentAPIView(SchoolAdminDetailAPIView):
    serializer_class = StudentSerializer
    model_class = Student

class ClassroomDetailView(generics.RetrieveAPIView):
    serializer_class = ClassroomSerializer
    permission_classes = [HasAccessOfSchoolBranch]

    def get_object(self):
        return get_object_or_404(Classroom, id=self.kwargs['pk'])


