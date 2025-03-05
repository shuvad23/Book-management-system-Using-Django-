from .models import Book
from django import forms 


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=[ 'title','author','description','published_year']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Book Title'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Author Name'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Book Descriptions'}),
            'published_year':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Published Year'})
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=[ 'title','author','description','published_year']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Book Title'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Author Name'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Book Descriptions'}),
            'published_year':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Published Year'})
        }