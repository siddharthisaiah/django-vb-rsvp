from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from datetime import datetime
from .models import Event, Attendee, Comment
from .forms import RsvpForm, CommentForm
# Create your views here.

@login_required
def index(request):
    now = datetime.date
    events = Event.objects.filter(event_datetime__gte=datetime.now())
    print(events)
    return render(request, 'events/index.html', {"events":events})


@login_required
def event(request, pk):
    event_details = get_object_or_404(Event, id=pk)
    attendees = Attendee.objects.filter(event=event_details)
    going = attendees[:event_details.max_attendees]
    waitlisted = attendees[event_details.max_attendees:]
    comments = Comment.objects.filter(event=event_details)

    # check if user is going to event
    user_is_going = Attendee.objects.filter(event=pk, user=request.user).exists()
    rsvp_form = RsvpForm(initial={'rsvp': user_is_going}) # dynamic inital values
    comment_form = CommentForm()
    
    context = {'title': 'RSVP - Event Details',
               'event_details':event_details,
               'attendees': attendees,
               'rsvp_form': rsvp_form,
               'comments': comments,
               'comment_form': comment_form,
               'going': going,
               'waitlisted': waitlisted}
    return render(request, 'events/event_details.html', context)


def rsvp(request, pk):
    # handle the POST form when a user RSVPs to an event going/not going
    if not request.method == 'POST':
        return HttpResponse(f"<h1>Access Not Allowed</h1>")

    form = RsvpForm(request.POST)

    if form.is_valid():
        # if the form has changed then update the attendees model with the user
        if form.cleaned_data['rsvp']: # user is going for the event
            rsvp = Attendee(event_id=pk, user=request.user)
            rsvp.save()
        else:
            Attendee.objects.filter(event=pk, user=request.user).delete()
        return redirect('event', pk=pk)
    else:
        return HttpResponse(f"<h1>Invalid Form</h1>")


def comment(request, pk):
    # handle the saving of a comment by the user
    if not request.method == 'POST':
        return HttpResponse('<h1>Access Is not allowed</h1>')

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        if comment:
            new_comment = Comment(event_id=pk, user=request.user, comment=comment)
            new_comment.save()
    
    return redirect('event', pk=pk)
