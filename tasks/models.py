from django.db import models
from base.models import BaseModel
from user.models import User
# Create your models here.
class Sub_Task(BaseModel):
    STATUS_CHOICE = (
        ('todo', 'To_Do'),
        ('in_progress', 'In_Progress'),
        ('review', 'Review'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel')
    )
    name = models.CharField(("Name"), max_length=50)
    description = models.TextField(("Description"))
    assigned = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(('STATUS'), max_length=20, choices=STATUS_CHOICE)  
    
    def __str__(self) -> str:
        return self.name 



class Task(BaseModel):
    name = models.CharField(("Name"), max_length=50)
    description = models.TextField(("Description"))
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    sub_task = models.ManyToManyField(Sub_Task)
    is_completed = models.CharField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    
    
    
    
    
    
 