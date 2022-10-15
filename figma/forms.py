from django import forms
from .models import User, UserProfile, Posts


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("Passwords Doesn't Match")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserPostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'