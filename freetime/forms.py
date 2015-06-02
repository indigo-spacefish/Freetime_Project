from django import forms
from freetime.models import Profile, Category, Activity, Goal, Record


class CategoryForm (forms.ModelForm):
    name = forms.CharField(max_length=255,
                           help_text="Custom Category Name",
                           )

    class Meta:
        model = Category
        fields = ('name',)


class ActivityForm (forms.ModelForm):
    name = forms.CharField(max_length=255,
                           help_text="Custom Activity Name",
                           )
    categories = forms.ModelChoiceField(queryset=Category,
                                        empty_label=None,
                                        to_field_name="name",
                                        )

    class Meta:
        model = Activity
        fields = ('name', 'categories',)


class GoalForm (forms.ModelForm):
    name = forms.CharField(max_length=255,
                           help_text="Custom Goal Name",
                           )
    activity = forms.ModelChoiceField(queryset=Activity,
                                      empty_label=None,
                                      to_field_name="name",
                                      )
    option_type = forms.IntegerField(max_value=4,
                                     min_value=1,
                                     )

    class Meta:
        model = Goal
        fields = ('name', 'activity', 'option_type',)


class RecordForm (forms.ModelForm):
    activity = forms.ModelChoiceField(queryset=Activity,
                                      empty_label=None,
                                      to_field_name="name",
                                      )
    date = forms.DateTimeField()

    class Meta:
        model = Record
        fields = ('activity', 'date',)
