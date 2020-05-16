from django.contrib import admin
from django import forms
from .models import Room, Event

class RoomAdminForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = '__all__'


class RoomAdmin(admin.ModelAdmin):
    form = RoomAdminForm
    list_display = ['name', 'size']
    #readonly_fields = ['name', 'size']

admin.site.register(Room, RoomAdmin)


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ['name', 'created', 'start', 'end']
    #readonly_fields = ['name', 'created', 'start', 'end']

admin.site.register(Event, EventAdmin)


