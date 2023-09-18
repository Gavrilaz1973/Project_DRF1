from rest_framework.relations import SlugRelatedField

from courses.models import Course
from lessons.models import Lesson
from rest_framework import serializers

from lessons.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video')]


class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'