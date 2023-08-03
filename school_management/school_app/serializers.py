from rest_framework import serializers
from .models import Classroom, School, SchoolBranch, Student, Teacher
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

class ClassroomSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    section = serializers.CharField(min_length=1, max_length=255, required=True,
                                     validators=[RegexValidator(r'^[A-Z]$', 'Only a single uppercase letter is allowed.')])

    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'branch']

class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabetic characters are allowed.')]
    )

    class Meta:
        model = School
        fields = ['id', 'name']

class SchoolBranchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabetic characters are allowed.')]
    )
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = SchoolBranch
        fields = ['id', 'name', 'school']

class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='classroom.branch.school.name')
    school_branch = serializers.ReadOnlyField(source='classroom.branch.name')
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    section = serializers.ReadOnlyField(source='classroom.section')
    age = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=255, required=True,
                                 validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabetic characters are allowed.')])
    date_of_birth = serializers.DateField()

    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'age', 'school_name', 'school_branch', 'classroom', 'section']

    def get_age(self, obj):
        today = date.today()
        return today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))

    def validate_date_of_birth(self, value):
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        
        if age < 3 or age > 100:
            raise serializers.ValidationError(_("Age must be between 3 and 100"))

        if value > today:
            raise serializers.ValidationError(_("Date of birth cannot be in the future"))

        return value

class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphabetic characters are allowed.')]
    )
    
    class Meta:
        model = Teacher
        fields = ['id', 'name']

 
