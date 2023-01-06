from django.db import models

# Create your models here.

class Jobs(models.Model):
    task_Name = models.CharField(max_length=50 , blank = False)
    amount = models.IntegerField( default = 0,blank = False)
    description = models.TextField(max_length=500 , blank = False, default = None)
    date_posted = models.DateField(auto_now_add=True)
    email = models.EmailField(verbose_name="Email", blank = False)
    provided_by = models.CharField(max_length=50 , blank = False)
    deadline = models.DateField(blank = False)
    is_completed = models.BooleanField(default = False)
    location = models.CharField(max_length=50 , blank = False)

    def __str__(self):
        return f"{self.Task_Name} - {self.Amount} - {self.Description} - {self.Date} - {self.email} - {self.provided_by} - {self.deadline} - {self.is_completed} - {self.location}"

