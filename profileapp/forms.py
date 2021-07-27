from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm): #import
    class Meta:
        model = Profile  #import
        fields = ['image', 'nickname', 'message']