from rest_framework import serializers
from .models import Classroom, School, SchoolBranch,Student,Teacher
from datetime import date

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'branch']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name']

class SchoolBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBranch
        fields = ['id', 'name', 'school']  

class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='classroom.branch.school.name')
    school_branch = serializers.ReadOnlyField(source='classroom.branch.name')
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all()) # Change this line
    section = serializers.ReadOnlyField(source='classroom.section')
    age = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'age', 'school_name', 'school_branch', 'classroom', 'section']

    def get_age(self, obj):
        today = date.today()
        return today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']
