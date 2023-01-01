from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    course_img=models.ImageField(upload_to='courseimg')
    course_name=models.CharField(max_length=100)
    course_des=models.TextField()
    course_duration=models.PositiveIntegerField()
    course_price=models.PositiveIntegerField()

    def __str__(self):
        return str(self.course_name)

class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Blog, on_delete=models.CASCADE)
  