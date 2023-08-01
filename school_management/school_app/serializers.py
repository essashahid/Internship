from rest_framework import serializers
from .models import Classroom, School, SchoolBranch, Student, Teacher
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class ClassroomSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    section = serializers.CharField(min_length=1, max_length=255, required=True) 

    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'branch']


class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = School
        fields = ['id', 'name']


class SchoolBranchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all()) 

    class Meta:
        model = SchoolBranch
        fields = ['id', 'name', 'school']


class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='classroom.branch.school.name')
    school_branch = serializers.ReadOnlyField(source='classroom.branch.name')
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all()) # Change this line
    section = serializers.ReadOnlyField(source='classroom.section')
    age = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=255, required=True)
    date_of_birth = serializers.DateField()

    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'age', 'school_name', 'school_branch', 'classroom', 'section']

    def get_age(self, obj):
        today = date.today()
        age = today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))
        if age < 3 or age > 100: # Age validation
            raise serializers.ValidationError(_("Age must be between 3 and 100"))
        return age

    def validate_date_of_birth(self, value):
        if value > date.today():
            raise serializers.ValidationError(_("Date of birth cannot be in the future"))
        return value

class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name']
