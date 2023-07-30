from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from .models import UserProfile, School, SchoolBranch,Teacher, Classroom, SchoolBranch,Student
from rest_framework.authtoken.models import Token

class SchoolTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, role=UserProfile.SCHOOL_ADMIN)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.school_data = {'name': 'Test School'}  # make sure this line is present and correctly indented

    def test_create_school(self):
        response = self.client.post(reverse('school_api'), self.school_data)
        if response.status_code == status.HTTP_201_CREATED:
            print("School creation test: success")
        else:
            print("School creation test: failure")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 1)
        self.assertEqual(School.objects.get().name, 'Test School')

    def test_update_school(self):
        response = self.client.post(reverse('school_api'), self.school_data)
        school = School.objects.get()
        new_data = {'name': 'Updated Test School'}
        response = self.client.put(reverse('school_detail_api', kwargs={'pk': school.id}), new_data)
        if response.status_code == status.HTTP_200_OK:
            print("School update test: success")
        else:
            print(f"School update test: failure, received status code {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_school(self):
        response = self.client.post(reverse('school_api'), self.school_data)
        school = School.objects.get()
        response = self.client.delete(reverse('school_detail_api', kwargs={'pk': school.id}))
        if response.status_code == status.HTTP_204_NO_CONTENT:
            print("School deletion test: success")
        else:
            print(f"School deletion test: failure, received status_code {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SchoolBranchTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user, role=UserProfile.SCHOOL_ADMIN)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.school = School.objects.create(name='Test School')  # create a school
        self.school_branch_data = {'name': 'Test School Branch', 'school': self.school.id}  # branch data

    def test_create_school_branch(self):
        response = self.client.post(reverse('school_branch_api'), self.school_branch_data)
        if response.status_code == status.HTTP_201_CREATED:
            print("School branch creation test: success")
        else:
            print("School branch creation test: failure")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SchoolBranch.objects.count(), 1)
        self.assertEqual(SchoolBranch.objects.get().name, 'Test School Branch')

    def test_update_school_branch(self):
        response = self.client.post(reverse('school_branch_api'), self.school_branch_data)
        school_branch = SchoolBranch.objects.get()
        new_data = {'name': 'Updated Test School Branch', 'school': self.school.id}
        response = self.client.put(reverse('school_branch_detail_api', kwargs={'pk': school_branch.id}), new_data)
        if response.status_code == status.HTTP_200_OK:
            print("School branch update test: success")
        else:
            print(f"School branch update test: failure, received status code {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_school_branch(self):
        response = self.client.post(reverse('school_branch_api'), self.school_branch_data)
        school_branch = SchoolBranch.objects.get()
        response = self.client.delete(reverse('school_branch_detail_api', kwargs={'pk': school_branch.id}))
        if response.status_code == status.HTTP_204_NO_CONTENT:
            print("School branch deletion test: success")
        else:
            print(f"School branch deletion test: failure, received status code {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


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



    

   