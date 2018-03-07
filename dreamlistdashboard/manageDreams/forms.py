from django import forms
from .models import Dream

class addDreamForm(forms.ModelForm):

    class Meta:
        model = Dream
        #checking a commit
        fields = ('title','description','deadline','weight','duration')

