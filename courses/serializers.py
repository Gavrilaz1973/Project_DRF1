from rest_framework.fields import SerializerMethodField

from courses.models import Course, Subscribe
from rest_framework import serializers

from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subscribe = SerializerMethodField()

    def get_is_subscribe(self, obj):
        for sub in Subscribe.objects.filter(course=obj.pk):
            for user in obj.user.all():
                if sub.user == user:
                    return True
        return False

    class Meta:
        model = Course
        fields = '__all__'




# class SubscribeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscribe
#         fields = '__all__'