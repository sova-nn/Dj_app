# -*- coding: utf-8 -*-

from django import forms

class SetMeForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('pub_date', u'Дата создания')), required=False)

    def clean(self):
        raise forms.ValidationError(u'Я не хочу искать и сортировать')

class QuesForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
