from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        labels = {
            'title':'Title'
        }


    def __init__(self, *args, **kwargs):
        super(NoteForm,self).__init__(*args,**kwargs)
        self.fields['category'].empty_label = "Choose.."


class NoteView(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        labels = {
            'title':'Title'
        }