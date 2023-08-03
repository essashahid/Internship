from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from school_app.models import Classroom, School, SchoolBranch, Student
import random
import string

class Command(BaseCommand):
    help = 'Generate data'

    def handle(self, *args, **options):
        # Create multiple schools
        for i in range(10):
            School.objects.create(name=f'School {i+1}')

        schools = School.objects.all()

        # Create multiple branches for each school
        for school in schools:
            for i in range(random.randint(5, 10)):
                SchoolBranch.objects.create(name=f'Branch {i+1} of {school.name}', school=school)

        branches = SchoolBranch.objects.all()

        # Create multiple classrooms for each branch
        for branch in branches:
            for i in range(random.randint(5, 10)):
                Classroom.objects.create(branch=branch, grade=random.randint(1, 12), section=random.choice(string.ascii_uppercase))

        classrooms = Classroom.objects.all()

        # Create multiple students for each classroom
        for classroom in classrooms:
            for i in range(random.randint(50, 100)):
                Student.objects.create(
                    name=f'Student {i+1} of {classroom.branch.name} {classroom.grade} {classroom.section}',
                    date_of_birth=timezone.now() - timedelta(days=random.randint(365*6, 365*18)),
                    classroom=classroom
                )

        self.stdout.write(self.style.SUCCESS('Random data generated successfully'))
