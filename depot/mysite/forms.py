
from django import forms
from models import *



class BookForm(forms.ModelForm):
	
    class Meta:
        model = Book	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)



class AuthorForm(forms.ModelForm):
	
    class Meta:
        model = Author	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)



class PublisherForm(forms.ModelForm):
	
    class Meta:
        model = Publisher	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)

