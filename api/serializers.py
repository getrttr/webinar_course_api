from rest_framework import serializers
from .models import Webinar, Course, Teacher, webinar_teacher


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class WebinarTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarTeacher
        fields = '__all__'
