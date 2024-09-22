from django import forms
from .models import Shop, Blog


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['image', 'title', 'info', 'price', 'slug']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'info']


class EmailForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
