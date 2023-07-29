from django.contrib import admin
from .models import Event, EventMember, EventRequest

admin.site.register(Event)
admin.site.register(EventMember)
admin.site.register(EventRequest)
# Register your models here.
