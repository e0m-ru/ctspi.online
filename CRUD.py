# CRUD classes as vievws.
from django.core.paginator import Paginator

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render
from .models import Event, EventLocation
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class EventCreateView(View):

    def get(self, request):
        return render(request, 'events/create.html')

    def post(self, request):
        try:
            event = Event.objects.create(
                title=request.POST['title'],
                s_dt=request.POST['s_dt'],
                e_dt=request.POST['e_dt'],
                descript=request.POST['descript'],
                location=request.POST['location'],
                author=User.objects.get(pk=request.user.id),
            )
            event.save()
            return HttpResponseRedirect(reverse('event-detail', args=[event.id]))
        except ValueError as e:
            return render(request, 'events/create.html',
                          {'error': f"Некорректные данные. {e}"})


class EventCreateView(PermissionRequiredMixin, EventCreateView):
    permission_required = ["ctspi.add_event"]


class EventDetailView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404("Событие не найдено.")
        context = {
            'title': f"Событие №{pk}",
            'event': event,
            'prev_page': request.META.get('HTTP_REFERER')
        }
        return render(request, 'events/detail.html', context)


class EventDetailView(PermissionRequiredMixin, EventDetailView):
    permission_required = ["ctspi.view_event"]


class EventUpdateView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            loc = EventLocation.objects.all()
        except Event.DoesNotExist:
            raise Http404(f"The event id:{pk} was not found.")
        return render(request, 'events/update.html', {'event': event, 'location': loc})

    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.title = request.POST['title']
        event.s_dt = request.POST['s_dt']
        event.e_dt = request.POST['e_dt']
        event.descript = request.POST['descript']
        event.location = EventLocation.objects.get(pk=request.POST['location'])
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


def blog(request):
    paginator = Paginator(Event.objects.all().order_by(
        '-s_dt'), 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'events': page_obj}
    return render(request, 'blog.html', context=context)
