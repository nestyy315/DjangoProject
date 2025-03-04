from django.db import models

# Create your models here.


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} {self.title} {self.description} {self.due_date} {self.status}"
