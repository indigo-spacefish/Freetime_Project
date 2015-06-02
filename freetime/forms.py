from django import forms
from freetime.models import Profile, Activity, Goal, Category, Record

class ActivityForm (forms.ModelForm):
    name = forms.CharField(max_length=255, help_text="Custom Activity Name")
    categories = forms.ModelChoiceField(queryset=Activity, empty_label=None, to_field_name="name")
    # user_starred
    sessions = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # Last Session

