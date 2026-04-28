from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Milestone, Project
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Milestone)
def check_phase1_complete(sender, instance, created, **kwargs):
    if instance.phase1:
        guide = instance.project.guide
        if guide:
            # Check if all projects under this guide have phase1 complete
            projects_under_guide = Project.objects.filter(guide=guide)
            all_complete = True
            for proj in projects_under_guide:
                if not hasattr(proj, 'milestone') or not proj.milestone.phase1:
                    all_complete = False
                    break
            
            if all_complete:
                logger.info(f"Notification: All teams under guide {guide.username} have completed Phase 1!")
                print(f"Notification: All teams under guide {guide.username} have completed Phase 1!")
