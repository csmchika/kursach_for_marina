from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import ListView

from .forms import EventForm, AddMemberForm
from .models import Event, EventMember


class EventListView(generic.ListView):
    model = Event
    template_name = "events/events.html"
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# Create your views here.
@login_required()
def create_event(request):
    user = request.user
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.save()
            messages.success(request, f'Event Successfully')
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form':form})


@login_required()
def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # event = Event.objects.get(id=event_id)
    # EventMember.objects.filter(event=event_id, user=request.user.id).exists()
    if EventMember.objects.filter(event=event_id, user=request.user.id).exists():
        exists = True
    else:
        exists = False
    context = {"event": event, "exists": exists}
    return render(request, "events/event-details.html", context)


@login_required
def search_events(request):
    query = request.GET.get('q')
    object_list = Event.objects.filter(tags__icontains=query)
    context ={
        'events': object_list,
        'q': query,
    }
    return render(request, "events/search_event.html", context)


@login_required
def event_delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.user:
        Event.objects.get(pk=event_id).delete()
    return redirect('home')


def members_list(request, pk):
    event = get_object_or_404(Event, pk=pk)
    # event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=pk)
    context = {
    'members': eventmember
    }
    return render(request, "events/members_list.html", context)


def delete_member(request, user_id, event_id):
    event_member = get_object_or_404(EventMember, user=user_id, event=event_id)
    event_member.delete()
    return HttpResponseRedirect('/event/{}'.format(event_id))


def add_member(request, user_id, event_id):
    EventMember.objects.get_or_create(
            user=request.user,
            event=Event.objects.get(id=event_id))
    return HttpResponseRedirect('/event/{}'.format(event_id))


class UserEventsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/user_events.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UserEventsListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['username'] = user
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(user=user).order_by('-date_posted')

