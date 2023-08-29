from djongo import models

class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
