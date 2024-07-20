# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment
from django.contrib.auth import get_user_model
from .models import Rating

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['comments', 'rating']
     
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        

        if email and password:
            self.user_cache = self.authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password.')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This account is inactive.')
        return self.cleaned_data

    def authenticate(self, email=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None




class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['star']