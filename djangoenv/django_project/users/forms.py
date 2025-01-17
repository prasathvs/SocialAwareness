from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from socialblog.models import Post

class UserRegisterForm(UserCreationForm):
     email = forms.EmailField()
     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
  class Meta:
        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']
class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields=('c_image',)
