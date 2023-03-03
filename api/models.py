from foxdb.db import models


class Webinar(models.Model):
    STATUS_CHOICES = (
        ('created', 'Создан'),
        ('started', 'Идет'),
        ('finished', 'Закончен'),
        ('canceled', 'Отменен')
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)


class WebinarTeacher(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='teachers')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
