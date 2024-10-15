from django.db import models

class Record(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.user.username + " - " + self.date.strftime("%Y-%m-%d")