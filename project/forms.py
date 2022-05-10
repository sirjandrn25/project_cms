from django import forms
from .models import *


class ProjectAddForm(forms.ModelForm):
    # document = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple':True}))
    class Meta:
        model = Project
        # fields = ['project_name','category','price_type','start_date','period_of_projects','budget','company','technology','description','skills','document']
        exclude =("end_date","progress","is_active","trash")
        widgets = {
            'project_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Project Name'}),
            # 'ref_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter reference link'}),
            'category':forms.Select(attrs={'class':'form-select','placeholder':'select category'}),
            'price_type':forms.Select(attrs={'class':'form-select','placeholder':'select suitable price'}),
            'start_date':forms.DateInput(attrs={'class':'form-control','type':'date','placeholder':'select suitable date'}),
            'period_of_projects':forms.Select(attrs={'class':'form-select'}),
            "budget":forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter project budget'}),
            'company':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter company name'}),
            'technology':forms.TextInput(attrs={'class':'form-control','placeholder':'techonology'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'write project description'}),
            'skills':forms.SelectMultiple(attrs={'class':'form-select'})
        }
    # def save(self,commit=True):
    #     data = self.cleaned_data
    

class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = ProjectDocument
        fields = "__all__"
        widgets = {
            "document":forms.ClearableFileInput(attrs={'class':'form-control','multiple':True})
        }
