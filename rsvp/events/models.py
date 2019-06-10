from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    event_datetime = models.DateField()
    max_attendees = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.event_datetime} - {self.max_attendees}'


class Comment(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    posted_at = models.DateField(auto_now_add=True)


class Attendee(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    
