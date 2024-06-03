from django.shortcuts import render
from .models import Event, Main_contents, Department
from .forms import SearchForm
from django.contrib.postgres.search import TrigramSimilarity
from .CRUD import *


def main(request):
    # index page
    url_path = request.path
    context = {'items': Main_contents.objects.all()}
    if url_path == '/':
        url_path = '/main'
    if url_path == '/departments':
        context.update({'depts': Department.objects.all()})
    try:
        post = Main_contents.objects.get(name=url_path[1:])
    except:
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

def player(request):
    return render(request, 'player.html')