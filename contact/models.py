from django.db import models


class Contact(models.Model):
    company = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
        return self.company
    class Meta:
            ordering = ['-created']
