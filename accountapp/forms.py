from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm): #import
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   #선택적 매개변수


        self.fields['username'].disabled = True



