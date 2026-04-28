from django.contrib import admin
from .models import Project, Milestone
from reversion.admin import VersionAdmin

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'guide', 'domain', 'marks')
    search_fields = ('title', 'team_members')
    list_filter = ('domain', 'guide')

@admin.register(Milestone)
class MilestoneAdmin(VersionAdmin):
    list_display = ('project', 'has_synopsis', 'has_phase1', 'has_phase2', 'has_final', 'has_publication')

    def has_synopsis(self, obj):
        return bool(obj.synopsis)
    has_synopsis.boolean = True
    def has_phase1(self, obj):
        return bool(obj.phase1)
    has_phase1.boolean = True
    def has_phase2(self, obj):
        return bool(obj.phase2)
    has_phase2.boolean = True
    def has_final(self, obj):
        return bool(obj.final_report)
    has_final.boolean = True
    def has_publication(self, obj):
        return bool(obj.publication)
    has_publication.boolean = True
