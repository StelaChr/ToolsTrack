from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import PasswordInput

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [ "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['password1'].help_text = "* Min 8 characters, at least one non-digit ."





