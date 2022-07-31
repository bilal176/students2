from django.db import models


# Create your models here.
class students(models.Model):
    name= models.CharField(max_length=100)
    reg= models.CharField(max_length=100)
    sec= models.CharField(max_length=100)
    project_name= models.CharField(max_length=100)
    project_field= models.CharField(max_length=100)
    superident= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
