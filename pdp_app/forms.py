from django import forms
from pdp_app.models import Post, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
   
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']