from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import reversion

DOMAIN_CHOICES = [
    ('AI', 'AI'),
    ('ML', 'ML'),
    ('IoT', 'IoT'),
]

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    team_members = models.TextField(help_text="List team members separated by commas")
    guide = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projects')
    domain = models.CharField(max_length=10, choices=DOMAIN_CHOICES)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.title

@reversion.register()
class Milestone(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='milestone')
    synopsis = models.FileField(upload_to='milestones/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'zip'])])
    phase1 = models.FileField(upload_to='milestones/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'zip'])])
    phase2 = models.FileField(upload_to='milestones/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'zip'])])
    final_report = models.FileField(upload_to='milestones/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'zip'])])
    publication = models.FileField(upload_to='milestones/', blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'zip'])])

    def __str__(self):
        return f"{self.project.title} Milestones"
