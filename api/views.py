from rest_framework import viewsets
from .models import Webinar, Course, Teacher, webinar_teacher
from .serializers import WebinarSerializer, CourseSerializer, TeacherSerializer, WebinarTeacherSerializer


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class WebinarTeacherViewSet(viewsets.ModelViewSet):
    queryset = WebinarTeacher.objects.all()
    serializer_class = WebinarTeacherSerializer
