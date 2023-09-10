from rest_framework.fields import SerializerMethodField

from courses.models import Course
from rest_framework import serializers

from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True )

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()



    class Meta:
        model = Course
        fields = '__all__'
