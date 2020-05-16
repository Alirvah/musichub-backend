import unittest
from django.urls import reverse
from django.test import Client
from .models import Room, Event
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_room(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["size"] = "size"
    defaults.update(**kwargs)
    return Room.objects.create(**defaults)


def create_event(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["start"] = "start"
    defaults["end"] = "end"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "room" not in defaults:
        defaults["room"] = create_room()
    return Event.objects.create(**defaults)


class RoomViewTest(unittest.TestCase):
    '''
    Tests for Room
    '''
    def setUp(self):
        self.client = Client()

    def test_list_room(self):
        url = reverse('bookit_room_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_room(self):
        url = reverse('bookit_room_create')
        data = {
            "name": "name",
            "size": "size",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_room(self):
        room = create_room()
        url = reverse('bookit_room_detail', args=[room.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_room(self):
        room = create_room()
        data = {
            "name": "name",
            "size": "size",
        }
        url = reverse('bookit_room_update', args=[room.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EventViewTest(unittest.TestCase):
    '''
    Tests for Event
    '''
    def setUp(self):
        self.client = Client()

    def test_list_event(self):
        url = reverse('bookit_event_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        url = reverse('bookit_event_create')
        data = {
            "name": "name",
            "start": "start",
            "end": "end",
            "user": create_django_contrib_auth_models_user().pk,
            "room": create_room().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_event(self):
        event = create_event()
        url = reverse('bookit_event_detail', args=[event.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        event = create_event()
        data = {
            "name": "name",
            "start": "start",
            "end": "end",
            "user": create_django_contrib_auth_models_user().pk,
            "room": create_room().pk,
        }
        url = reverse('bookit_event_update', args=[event.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


