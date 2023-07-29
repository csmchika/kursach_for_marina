from datetime import datetime
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


class Event(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    pic = models.ImageField(default='path/to/event-img/default.png', upload_to='path/to/event-img')
    date_posted = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("events:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventMember(models.Model):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_members"
    )

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)


class EventRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user_event', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user_event', on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)