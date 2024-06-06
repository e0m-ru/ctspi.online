from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django import forms
from datetime import datetime
from .models import Event
from django.contrib.auth.models import User
from django.urls import reverse


class SearchForm(forms.Form):
    query = forms.CharField(label="поиск")


# input type = "datetime-local"
class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateTimeLocalField(forms.DateTimeField):
    # Set DATETIME_INPUT_FORMATS here because, if USE_L10N
    # is True, the locale-dictated format will be applied
    # instead of settings.DATETIME_INPUT_FORMATS.
    # See also:
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats
    input_formats = [
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M",
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")


class EventTitleForm(forms.Form):
    # form 1
    title = forms.CharField(
        label='Название',
        max_length=100,
        min_length=3,
        strip=True,
    )


class EventDTForm(forms.Form):
    # form 2
    s_dt = DateTimeLocalField(
        label='Дата и Время',
        required=True,
    )
    e_dt = DateTimeLocalField(
        label='Дата и Время',
    )


class EventCategoryForm(forms.Form):
    # form 4
    # category =
    descript = forms.CharField(
        label='Описание',
        widget=forms.Textarea(),
    )


class EventDescriptionForm(forms.Form):
    # form 5
    description = forms.CharField(
        label='Место',
    )


class EventWizard(SessionWizardView):
    template_name = "EventWizardForm.html"
    form_list = [EventTitleForm, EventDTForm,
                 EventCategoryForm, EventDescriptionForm]

    def done(self, form_list, **kwargs):
        form_data = dict()
        for form in form_list:
            form_data.update(form.cleaned_data)
        # [form.cleaned_data for form in form_list]
        print(form_data)
        # обработка данных
        try:
            event = Event.objects.create(
                title=form_data['title'],
                s_dt=form_data['s_dt'],
                e_dt=form_data['e_dt'],
                descript=form_data['descript'],
                author=User.objects.get(pk=1),
            )
            event.save()
            return HttpResponseRedirect(reverse('event-detail', args=[event.id]))
        except ValueError as e:
            return e
        
        return HttpResponseRedirect('/finished/')
