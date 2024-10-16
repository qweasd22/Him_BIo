from django.db import models

class UserFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name - " + self.name + ", email - " + self.email