from lessons.models import Lesson
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    model = Lesson
    fields = '__all__'
