from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Project, Milestone
from .forms import ProjectRegistrationForm, MilestoneUploadForm
from django.contrib import messages
import csv

def home(request):
    return render(request, 'projects/home.html')

def register_project(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        if form.is_valid():
            project = form.save()
            Milestone.objects.create(project=project)
            messages.success(request, 'Project registered successfully!')
            return redirect('upload_milestone', project_id=project.id)
    else:
        form = ProjectRegistrationForm()
    return render(request, 'projects/register.html', {'form': form})

def upload_milestone(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    milestone = project.milestone
    if request.method == 'POST':
        form = MilestoneUploadForm(request.POST, request.FILES, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('upload_milestone', project_id=project.id)
    else:
        form = MilestoneUploadForm(instance=milestone)
    return render(request, 'milestones/upload.html', {'form': form, 'project': project})

@login_required
def guide_dashboard(request):
    teams = Project.objects.filter(guide=request.user)
    
    # Calculate progress for each team
    teams_with_progress = []
    labels = []
    data = []
    
    for team in teams:
        m = team.milestone
        completed = sum(bool(getattr(m, field)) for field in ['synopsis', 'phase1', 'phase2', 'final_report', 'publication'])
        progress = (completed / 5) * 100
        teams_with_progress.append({'project': team, 'progress': progress})
        labels.append(team.title)
        data.append(progress)
        
    context = {
        'teams': teams_with_progress,
        'chart_labels': labels,
        'chart_data': data,
    }
    return render(request, 'projects/dashboard.html', context)

def export_csv(request):
    domain = request.GET.get('domain')
    guide_id = request.GET.get('guide_id')
    
    queryset = Project.objects.all()
    if domain:
        queryset = queryset.filter(domain=domain)
    if guide_id:
        queryset = queryset.filter(guide_id=guide_id)
        
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects_export.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Title', 'Team Members', 'Marks', 'Status (Phase 1 Complete)'])
    
    for project in queryset:
        status = "Yes" if bool(project.milestone.phase1) else "No"
        writer.writerow([project.title, project.team_members, project.marks, status])
        
    return response

def api_check_title(request):
    query = request.GET.get('q', '')
    exists = Project.objects.filter(title__iexact=query).exists()
    return JsonResponse({'exists': exists})
