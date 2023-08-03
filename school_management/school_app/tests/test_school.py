from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from school_app.models import UserProfile, School, SchoolBranch,Teacher, Classroom, SchoolBranch,Student
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
