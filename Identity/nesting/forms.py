from django import forms
from nesting.models import Identity_unique
from nesting.models import Symptom_relation


class Identity_Form(forms.ModelForm):

    NIS = forms.CharField(
                    widget=forms.TextInput(
                            attrs={

                                'placeholder': 'Enter NIS',
                                'class' : 'form-control'
                            }
                )
    )

    first_Name = forms.CharField(
                widget=forms.TextInput(
                        attrs={

                            'placeholder': 'Enter First Name',
                            'class' : 'form-control'
                        }
            )
    )
    last_Name = forms.CharField(

       widget=forms.TextInput(
               attrs={

                   'placeholder': 'Enter Last Name',
                   'class' : 'form-control'
               }
        )
    )

    location = forms.CharField(

            widget=forms.TextInput(
                        attrs= {

                        'placeholder':'Enter Address',
                        'class':'form-control'

                        }
            )
    )

    date_of_birth = forms.DateField(

                widget=forms.TextInput(
                            attrs= {

                            'placeholder' : 'Enter Birthday',
                            'class':'form-control'

                            }
                ),
        )

    contact = forms.CharField(

                    widget=forms.TextInput(
                                attrs= {

                                'placeholder':'Enter Contact',
                                'class':'form-control'

                                }
                    )
            )


    class Meta:

        model = Identity_unique

        fields = ('NIS', 'first_Name', 'last_Name', 'location', 'date_of_birth', 'contact',)




class Symptom_Form(forms.ModelForm):


                symptom_description = forms.CharField(

                widget=forms.Textarea(
                            attrs= {

                            'placeholder':'Symptom description',
                            'class':'form-control'

                            }
                )
    )

                symptom_name = forms.CharField(


                    widget=forms.TextInput(
                                attrs= {

                                'placeholder':'Symptom Name',
                                'class':'form-control'

                                }
                    )

                )

                class Meta:

                    model = Symptom_relation

                    fields = ('symptom_name', 'symptom_description',)
