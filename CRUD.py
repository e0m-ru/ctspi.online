# CRUD classes as vievws.

from django.views import View
from django.shortcuts import render
from .models import Event
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


class EventCreateView(View):
    """Создание нового события.
    """

    def get(self, request):
        return render(request, 'events/create.html')

    def post(self, request):
        title = request.POST['title']
        s_dt = request.POST['s_dt']
        e_dt = request.POST['e_dt']
        descript = request.POST['descript']
        cat = request.POST['cat']

        try:
            event = Event.objects.create(
                title=title,
                s_dt=s_dt,
                e_dt=e_dt,
                descript=descript,
                cat=cat
            )
            return HttpResponseRedirect(reverse('event-detail', args=[event.id]))
        except ValueError:
            return render(request, 'events/create.html', {'error': "Некорректные данные."})


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
