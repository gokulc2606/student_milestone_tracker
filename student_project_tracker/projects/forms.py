from django import forms
from .models import Project, Milestone

class ProjectRegistrationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'team_members', 'guide', 'domain']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_title'}),
            'team_members': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'guide': forms.Select(attrs={'class': 'form-select'}),
            'domain': forms.Select(attrs={'class': 'form-select'}),
        }

class MilestoneUploadForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['synopsis', 'phase1', 'phase2', 'final_report', 'publication']
        widgets = {
            'synopsis': forms.FileInput(attrs={'class': 'form-control'}),
            'phase1': forms.FileInput(attrs={'class': 'form-control'}),
            'phase2': forms.FileInput(attrs={'class': 'form-control'}),
            'final_report': forms.FileInput(attrs={'class': 'form-control'}),
            'publication': forms.FileInput(attrs={'class': 'form-control'}),
        }
