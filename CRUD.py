# CRUD classes as vievws.

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views import View
from django.shortcuts import render
from .models import Event
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin




class EventCreateView(View):
    """Создание нового события.
    """

    def get(self, request):
        return render(request, 'events/create.html')

    def post(self, request):
        author_id = request.user.id
        title = request.POST['title']
        s_dt = request.POST['s_dt']
        e_dt = request.POST['e_dt']
        descript = request.POST['descript']
        # cat = request.POST['cat']

        try:
            event = Event.objects.create(
                title=title,
                s_dt=s_dt,
                e_dt=e_dt,
                descript=descript,
                author_id=1,
            )
            return HttpResponseRedirect(reverse('event-detail', args=[event.id]))
        except ValueError:
            return render(request, 'events/create.html', {'error': "Некорректные данные."})

class EventCreateView(PermissionRequiredMixin, EventCreateView):
    permission_required = ["ctspi.add_event"]


class EventDetailView(View):
    """Детали события.
    """

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404(
                "Событие не найдено.")
        context = {
            'event': event
        }
        return render(request, 'events/detail.html', context)


class EventDetailView(PermissionRequiredMixin, EventDetailView):
    permission_required = ["ctspi.view_event"]

class EventUpdateView(View):
    """Updating the event.
    """
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404(f"The event id:{pk} was not found.")
        return render(request, 'events/update.html', {'event': event})

    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.title = request.POST['title']
        event.s_dt = request.POST['s_dt']
        event.e_dt = request.POST['e_dt']
        event.descript = request.POST['descript']
        event.category = request.POST['category']
        event.save()
        return HttpResponseRedirect(reverse('event-detail', args=[event.id]))


class EventUpdateView(PermissionRequiredMixin, EventUpdateView):
    permission_required = ["ctspi.change_event"]

class EventDeleteView(View):
    """Removing the event."""

    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        context = {
            'event': event
        }
        return render(request, 'events/delete.html', context)

    def post(self, _, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return HttpResponseRedirect(reverse('event-list'))


class EventDeleteView(PermissionRequiredMixin, EventDeleteView):
    permission_required = ["ctspi.delete_event"]
