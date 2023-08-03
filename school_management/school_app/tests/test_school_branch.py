from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from school_app.models import UserProfile, School, SchoolBranch,Teacher, Classroom, SchoolBranch,Student
from rest_framework.authtoken.models import Token

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