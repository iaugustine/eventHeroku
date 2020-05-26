from django import forms
from .models import *

class DateIn(forms.DateInput):
    input_type = 'date'

class TimeIn(forms.TimeInput):
    input_type = 'time'

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'
        #fields['event'].disabled = True
        labels = {
            'event' : 'Registering for Event:'
        }


    def __init__(self, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        # self.fields['event'].disabled = True


class EventForm(forms.ModelForm):
    e_date = forms.DateField(widget=DateIn)
    e_time = forms.TimeField(widget=TimeIn)
    class Meta:
        model = Events
        fields = '__all__'

        labels = {
            'e_title' : 'Event Title',
            'e_description' : 'Event Description',
            'e_city' : 'City',
            'e_date' : 'Date',
            'e_time' : 'Time',
            'e_capacity' : 'Event Capacity',
            'e_attending' : 'People Attending',
            'e_vacancy' : 'Empty Seats',
            'e_price'   :   'Ticket Price',
            'e_duration' : 'Event Length',
            'e_status' : 'Status',
            'e_type' : 'Event Type'
        }
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['e_status'].empty_label= "Select"
        self.fields['e_type'].empty_label = "Select"
        self.fields['e_attending'].required = False
        self.fields['e_duration'].required = False
        self.fields['e_vacancy'].required = False
        self.fields['e_sales'].required = False




