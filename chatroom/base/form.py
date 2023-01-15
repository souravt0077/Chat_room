from django.forms import ModelForm
from .models import Room

class roomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['participants','host']