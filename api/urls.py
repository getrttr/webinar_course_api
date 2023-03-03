from django.urls import path, include
from rest_framework import routers
from .views import WebinarViewSet, CourseViewSet, TeacherViewSet, WebinarTeacherViewSet

router = routers.DefaultRouter()
router.register(r'webinars', WebinarViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'webinar_teachers', WebinarTeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
