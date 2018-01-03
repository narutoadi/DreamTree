from django import forms
from .models import Dream

class addDreamForm(forms.ModelForm):

    class Meta:
        model = Dream
        fields = ('title','description','deadline','weight','duration',)

