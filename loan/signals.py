from django.db.models.signals import post_save
from django.dispatch import receiver
from loan.tasks import update_loan_status_task

from .models import Loan

@receiver(post_save, sender=Loan)
def loan_post_save(sender, instance: Loan, created, **kwargs):
    if created:
        try:
            update_loan_status_task.delay(id=instance.pk)
        except Exception as e:
            print(f'Error trying to get Loan API status for {instance}: {str(e)}')
