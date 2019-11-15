from django.db import models

# Create your models here.
class Users(models.Model):
    job_seeker_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ranking = models.FloatField()

    def upload_resume(self, filename):
        path = 'hrm/resume/{}'.format(filename)
        return path

    resume = models.ImageField(upload_to=upload_resume, null=True, blank=True)

    def __str__(self):
        return f"{self.job_seeker_id}: {self.name}"

