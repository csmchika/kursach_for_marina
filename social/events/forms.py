from django import forms
from django.forms import ModelForm, DateInput

from .models import EventMember, Event


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "tags", "pic", "date"]
        # datetime-local is a HTML5 input type
        widgets = {
            # "title": forms.TextInput(
            #     attrs={"class": "form-control", "placeholder": "Enter event title"}
            # ),
            # "description": forms.Textarea(
            #     attrs={
            #         "class": "form-control",
            #         "placeholder": "Enter event description",
            #     }
            # ),
            "date": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%d",
            ),
        }
        exclude = ["user"]

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     # input_formats to parse HTML5 datetime-local input to datetime field
    #     self.fields["date_posted"].input_formats = ("%Y-%m-%dT%H:%M",)
    #     self.fields["date"].input_formats = ("%Y-%m-%dT%H:%M",)