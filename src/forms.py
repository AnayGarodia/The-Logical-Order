from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class UploadFileForm(forms.Form):
    image = forms.FileField(label="choose a file")
