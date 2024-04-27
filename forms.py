from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="поиск", help_text="помощь", initial="начальное значение")
