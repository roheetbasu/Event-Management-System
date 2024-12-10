from django.db import models
from django.contrib.auth.models import User
class Space(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=50)
    amenitites = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    EVENT_STATUS = [('PENDING','Pending'),('APPROVED','Approved'),('REJECTED','Rejected')]
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name = 'bookings')
    # organizer = models.ForeignKey(User, on_delete=modles.CASCADE, related_name = 'bookings')
    event_name = models.CharField(max_length = 200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participant_count = models.PositiveIntegerField()
    status = models.CharField(max_length = 10, choices=EVENT_STATUS, default= 'pending')

