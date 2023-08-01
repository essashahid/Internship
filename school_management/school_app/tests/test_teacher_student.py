from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from school_app.models import UserProfile, School, SchoolBranch,Teacher, Classroom, SchoolBranch,Student
from rest_framework.authtoken.models import Token


class Teacher_StudentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, role=UserProfile.SCHOOL_ADMIN)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.school = School.objects.create(name='Test School')  # create a school
        self.branch = SchoolBranch.objects.create(school=self.school, name="Test Branch")
        self.classroom = Classroom.objects.create(grade=1, branch=self.branch, section='abc')  

        self.teacher_data = {'name': 'Test Teacher', 'school': self.school.id}

        self.student_data = {
            "classroom": self.classroom.id,
            "name": "John Doe",
            "date_of_birth": "2000-01-01",
            "address": "123 Main St",
        }


    def test_create_teacher(self):
        response = self.client.post(reverse('teacher_api'), self.teacher_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Teacher Creation test: success")

    def test_update_teacher(self):
        response = self.client.post(reverse('teacher_api'), self.teacher_data)
        teacher = Teacher.objects.get()
        new_data = {'name': 'Updated Test Teacher', 'school': self.school.id}
        response = self.client.put(reverse('teacher_detail_api', kwargs={'pk': teacher.id}), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Teacher Update test: success")

    def test_delete_teacher(self):
        response = self.client.post(reverse('teacher_api'), self.teacher_data)
        teacher = Teacher.objects.get()
        response = self.client.delete(reverse('teacher_detail_api', kwargs={'pk': teacher.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Teacher deletion test: success")


    def test_create_student(self):
        response = self.client.post(reverse('student_api'), self.student_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Student creation test: success")


    def test_update_student(self):
        response = self.client.post(reverse('student_api'), self.student_data)
        student = Student.objects.get()
        update_data = self.student_data.copy()
        update_data['name'] = 'Updated Test Student'
        response = self.client.put(reverse('student_detail_api', kwargs={'pk': student.id}), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Student Update test: success")


    def test_delete_student(self):
        response = self.client.post(reverse('student_api'), self.student_data)
        student = Student.objects.get()
        response = self.client.delete(reverse('student_detail_api', kwargs={'pk': student.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Student Delete test: success")



    