from veganapp.models import VeganFood
from django import forms


class AddFood(forms.ModelForm):
    class Meta:
        model = VeganFood
        fields = ['name','image','desc','organ','slug']
