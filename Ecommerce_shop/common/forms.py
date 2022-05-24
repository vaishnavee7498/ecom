from django import forms
from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate
# from common.models import User



# from manager_app.models import Users

# User = get_user_model()
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(max_length=10, widget=forms.TextInput())
    password = forms.CharField(max_length=8, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 8:
                raise forms.ValidationError(
                    'Password must be at least 8 characters long!')
        return password

# login form
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     print(email)
    #     print(password)
    #     if email and password:
    #         user = authenticate(email=email, password=password)
    #         print('user')
    #         print(user)
    #         if not user:
    #             raise forms.ValidationError("user does not existtttt")
    #         pwd = User.objects.get(email=email)
    #         if not pwd.check_password(password):
    #             raise forms.ValidationError("invalid password")
    #     return self.cleaned_data

