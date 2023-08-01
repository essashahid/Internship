from django.test import TestCase
from school_app.serializers import ClassroomSerializer, SchoolSerializer, SchoolBranchSerializer, StudentSerializer, TeacherSerializer
from datetime import date

from school_app.models import Classroom, SchoolBranch,School

class ValidatorsTest(TestCase):
    
    def setUp(self):
        self.school = School.objects.create(name='School Name') # Create school object
        self.branch = SchoolBranch.objects.create(name='Branch Name', school=self.school) # Create branch object with the school instance
        self.classroom = Classroom.objects.create(grade=5, section='A', branch=self.branch) # Create classroom object


    def test_classroom_serializer(self):
        valid_data = {'grade': 5, 'section': 'A', 'branch': self.branch.id}
        serializer = ClassroomSerializer(data=valid_data)
        print("Testing valid classroom data:", serializer.is_valid())
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid(), "Classroom valid data failed.")

        invalid_data = {'grade': 13, 'section': 'A', 'branch': 1}
        serializer = ClassroomSerializer(data=invalid_data)
        print("Testing invalid classroom data with invalid grade:", serializer.is_valid())
        self.assertFalse(serializer.is_valid(), "Classroom invalid grade failed.")

        invalid_data = {'grade': 5, 'section': 'AB', 'branch': 1}
        serializer = ClassroomSerializer(data=invalid_data)
        print("Testing invalid classroom data with invalid section:", serializer.is_valid())
        self.assertFalse(serializer.is_valid(), "Classroom invalid section failed.")

    def test_school_serializer(self):

        valid_data = {'name': 'Test School'}
        serializer = SchoolSerializer(data=valid_data)
        print("Testing valid school data:", serializer.is_valid())
        self.assertTrue(serializer.is_valid(), "School valid data failed.")

        invalid_data = {'name': 'Test123'}
        serializer = SchoolSerializer(data=invalid_data)
        print("Testing invalid school data with invalid name:", serializer.is_valid())
        self.assertFalse(serializer.is_valid(), "School invalid name failed.")

    def test_student_serializer(self):
        
        valid_data = {'name': 'John Doe', 'date_of_birth': '2010-01-01', 'classroom': 1}
        serializer = StudentSerializer(data=valid_data)
        print("Testing valid student data with valid data:", serializer.is_valid())

        self.assertTrue(serializer.is_valid(), "Student valid data failed.")

        invalid_data = {'name': 'John Doe', 'date_of_birth': '3000-01-01', 'classroom': 1}
        serializer = StudentSerializer(data=invalid_data)
        print("Testing invalid student data with invalid date of birth:", serializer.is_valid())
        self.assertFalse(serializer.is_valid(), "Student future date of birth failed.")

