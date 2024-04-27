from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Event, Main_contents, Department
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import View
from django.urls import reverse
from ctspi.forms import SearchForm
# from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity


def main(request):
    url_path = request.path
    context = {'items': Main_contents.objects.all()}
    if url_path == '/':
        url_path = '/main'
    if url_path == '/departments':
        context.update({'depts': Department.objects.all()})
    try:
        post = Main_contents.objects.get(name=url_path[1:])
    except:
        pass
        return ctspi_404(request)
    context.update({'post': post})
    return render(request, 'index.html', context)


def departments(request):
    try:
        post = Department.objects.get(name=request.path.split('/')[-1])
    except:
        return ctspi_404(request)
    return render(request, 'index.html', context={'r': request, 'post': post, 'depts': Department.objects.all(), 'items': Main_contents.objects.all()})


def ctspi_404(request):
    return render(request, '404.html', status=404, context={'name': request.path})


@login_required(login_url="/login/")
def anons(request):
    context = {'items': Main_contents.objects.all()}
    return render(request, 'anons.html', context=context)


def write_anons(request):
    with open(f'static/anons.csv', 'w', encoding='utf-8') as file:
        file.write(resp := str(request.body.decode('utf-8')))
    # Создаем свой кастомный ответ
    custom_response = HttpResponse(resp, content_type="text/plain")
    custom_response.status_code = 200
    return custom_response


def blog(request):
    paginator = Paginator(Event.objects.all().order_by(
        '-start_time'), 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'events': page_obj}
    return render(request, 'blog.html', context=context)


# CRUD
class EventListView(View):
    """Список событий.
    """

    def get(self, request):
        events = Event.objects.all()
        context = {
            'events': events
        }
        return render(request, 'events/list.html', context)


class EventCreateView(View):
    """Создание нового события.
    """

    def get(self, request):
        return render(request, 'events/create.html')

    def post(self, request):
        title = request.POST['title']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        descript = request.POST['descript']
        cat = request.POST['cat']

        try:
            event = Event.objects.create(
                title=title,
                start_time=start_time,
                end_time=end_time,
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
        title = request.POST['title']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        descript = request.POST['descript']
        cat = request.POST['cat']
        event.title = title
        event.start_time = start_time
        event.end_time = end_time
        event.descript = descript
        event.cat = cat
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


def event_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        # search_vector = SearchVector('title', 'descript', config='russian')
        # search_query = SearchQuery(query, config='russian')
        results = Event.objects.annotate(similarity=TrigramSimilarity(
            'title', query),).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})
