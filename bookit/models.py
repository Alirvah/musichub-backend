from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Room(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    size = models.TextField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('bookit_room_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('bookit_room_update', args=(self.pk,))


class Event(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    start = models.DateTimeField()
    end = models.DateTimeField()

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="events", 
    )
    room = models.ForeignKey(
        'bookit.Room',
        on_delete=models.CASCADE, related_name="events", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('bookit_event_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('bookit_event_update', args=(self.pk,))


