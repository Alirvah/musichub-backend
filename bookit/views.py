from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Room, Event
from .forms import RoomForm, EventForm


#from django.shortcuts import render
#from django.urls import reverse_lazy
#from django.views.generic import CreateView
#from bookit.forms import SignUpForm
#
## Sign Up View
#class SignUpView(CreateView):
#    form_class = SignUpForm
#    success_url = reverse_lazy('login')
#    template_name = 'bookit/signup.html'



class RoomListView(ListView):
    model = Room


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm


class RoomDetailView(DetailView):
    model = Room


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm


class EventListView(ListView):
    model = Event


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm


class EventDetailView(DetailView):
    model = Event


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm

