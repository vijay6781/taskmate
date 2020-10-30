from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasklist(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=400)
    done = models.BooleanField(default=False)
     
    
        # renames the instances of the model 
        # with their title name 
    def __str__(self): 
        return self.task +" . "+ str(self.done)
     
     
     

    

