from django import forms
from nesting.models import Identity_unique

class Identity_form(forms.ModelForm):

    NIS = forms.CharField()


    class Meta:

        model = Identity_unique

        fields = ('NIS',)
