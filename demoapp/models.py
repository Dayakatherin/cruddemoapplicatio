from django.db import models
class user(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    user_name = models.CharField(max_length = 50)
    email_id = models.EmailField(max_length=50)
    password=models.CharField(max_length=100)

    
