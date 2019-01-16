from django import forms
from django.forms import ModelForm
from .models import User, Group


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'grupy']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["grupy"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["grupy"].queryset = Group.objects.all()


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['nazwa_grupy']

    #grupa = forms.ModelMultipleChoiceField(queryset=User.objects.all())
