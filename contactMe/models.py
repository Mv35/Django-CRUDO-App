from django.db import models


class ContactFormModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=100, choices=[
                                ('question', 'Question'), ('other', 'Other')])
    subject = models.CharField(max_length=100, default='')
    body = models.TextField()

    def __str__(self):
        return self.name
