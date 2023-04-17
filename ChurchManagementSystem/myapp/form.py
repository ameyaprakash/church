from django import forms
from .models import staff,marriage,baptism,confession,prayerdetails,sermons,participation,events,funddetails,eventreport
from django.forms.widgets import DateInput,TimeInput
class staffForm(forms.ModelForm):
    class Meta:
        model=staff
        fields="__all__"
        

class marriagForm(forms.ModelForm):
    class Meta:
        model=marriage
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class baptismForm(forms.ModelForm):
    class Meta:
        model=baptism
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class confessionForm(forms.ModelForm):
    class Meta:
        model=confession
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class prayerdetailsForm(forms.ModelForm):
    class Meta:
        model=prayerdetails
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class sermonsdetailsForm(forms.ModelForm):
    class Meta:
        model=sermons
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class eventsForm(forms.ModelForm):
    class Meta:
        model=events
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class paricipantsForm(forms.ModelForm):
    class Meta:
        model=participation
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class funddetailsForm(forms.ModelForm):
    class Meta:
        model=funddetails
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"})
            ,"time":TimeInput(attrs={'type':"time"})
        }

class reportForm(forms.ModelForm):
    class Meta:
        model=eventreport
        fields="__all__"