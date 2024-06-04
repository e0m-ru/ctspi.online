from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django import forms
from datetime import datetime


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


class EventTitle(forms.Form):
    # form 1
    title = forms.CharField(
        label='Заголовок',
        max_length=100,
        min_length=3,
        strip=True,
    )
    

class EventTitle2(forms.Form):
    date_Time = DateTimeLocalField(
        required=bool,
        label='Дата и время',
        initial=datetime.now(),
        
    )


class EventDescription(forms.Form):
    # form 2
    description = forms.CharField(
        widget=forms.Textarea(),
    )


class EventWizard(SessionWizardView):
    template_name = "EventWizardForm.html"
    form_list = [EventTitle, EventTitle2, EventDescription]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        # обработка данных

        return HttpResponseRedirect('/finished/')
