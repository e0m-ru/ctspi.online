from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Main_contents
from django.shortcuts import render

def write_anons(request):
    with open(f'static/anons.csv', 'w', encoding='utf-8') as file:
        file.write(resp := str(request.body.decode('utf-8')))
    # Создаем свой кастомный ответ
    custom_response = HttpResponse(resp, content_type="text/plain")
    custom_response.status_code = 200
    return custom_response


@login_required(login_url="/login/")
def anons(request):
    context = {'items': Main_contents.objects.all()}
    return render(request, 'anons.html', context=context)
