from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from school_app.models import SchoolBranch, User,School,UserProfile,Classroom
from django.contrib.auth.models import Group
from rest_framework.test import APIClient



class SchoolBranchAccessTest(APITestCase):
    def setUp(self):

        self.branch_manager_group = Group.objects.create(name='Branch Manager')
        
        self.branch_manager1_user = User.objects.create(username='manager1')
        self.branch_manager1 = UserProfile.objects.create(user=self.branch_manager1_user, role=UserProfile.SCHOOL_BRANCH_MANAGER)
        self.branch_manager1_user.groups.add(self.branch_manager_group)

        self.branch_manager2_user = User.objects.create(username='manager2')
        self.branch_manager2 = UserProfile.objects.create(user=self.branch_manager2_user, role=UserProfile.SCHOOL_BRANCH_MANAGER)
        self.branch_manager2_user.groups.add(self.branch_manager_group)

        self.other_user = User.objects.create(username='otheruser')

        self.school = School.objects.create(name='Test School')

        self.school_branch1 = SchoolBranch.objects.create(name='Branch 1', school=self.school)
        self.school_branch2 = SchoolBranch.objects.create(name='Branch 2', school=self.school)

        self.school_branch1.branch_managers.set([self.branch_manager1])
        self.school_branch2.branch_managers.set([self.branch_manager2])


    def test_access_with_permission(self):
        classroom = Classroom.objects.create(branch=self.school_branch1, grade=10, section='A')

        url = reverse('classroom-detail', kwargs={'pk': classroom.id})
        self.client.force_authenticate(user=self.branch_manager1)
        response = self.client.get(url)
        # print("content of response", response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_access_without_permission(self):
        classroom = Classroom.objects.create(branch=self.school_branch1, grade=10, section='A')
        url = reverse('classroom-detail', kwargs={'pk': classroom.id})
        self.client.force_authenticate(user=self.branch_manager2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print("Permissions Test Passed!")

