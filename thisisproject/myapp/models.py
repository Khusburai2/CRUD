import datetime
import os
from django.db import models

#  For storing the location of the image making function 
def image_function_loca(request,filename):
    newfilename = filename
    time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = newfilename + time 
    return os.path.join('image_uploads',filename)



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to=image_function_loca, blank=True)

    def __str__(self):
        return self.title
    
    # py manage.py createsuperuser
    # admin site chlaunu lai superuser create garnu parcha mathi ko command lea 
