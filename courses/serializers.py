from courses.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    model = Course
    fields = '__all__'


