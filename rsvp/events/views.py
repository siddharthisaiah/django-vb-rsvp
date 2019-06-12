from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import datetime
from .models import Event, Attendee
# Create your views here.

@login_required
def index(request):
    now = datetime.date
    events = Event.objects.all() #Event.objects.filter(event_datetime__gte=datetime.now())
    print(events)
    return render(request, 'events/index.html', {"events":events})


@login_required
def event(request, pk):
    event_details = get_object_or_404(Event, id=pk)
    attendees = Attendee.objects.filter(event=event_details)
    print(attendees)
    context = {'title': 'RSVP - Event Details', 'event_details':event_details, 'attendees': attendees}
    return render(request, 'events/event_details.html', context)
