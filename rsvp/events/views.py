from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Event
# Create your views here.

@login_required
def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {events:events})


@login_required
def event(request, pk):
    context = {'title': 'RSVP - Event Details'}
    return render(request, 'events/event_details.html', context)
