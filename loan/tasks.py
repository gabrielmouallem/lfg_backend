from __future__ import absolute_import, unicode_literals
import json
import requests
from loan.models import Loan
from celery import shared_task

@shared_task
def update_loan_status_task(id):
    print("Updating loan status...")
    try:
        loan = Loan.objects.get(id=id)
        name = loan.name
        document = loan.cpf
        response = requests.post('https://loan-processor.digitalsys.com.br/api/v1/loan/', {"name": name, "document": document})
        response.raise_for_status()

        data_bytes = response.content
        data_str = data_bytes.decode('utf-8')
        data_dict = json.loads(data_str)

        approved = data_dict['approved']
        status = ''
        if approved:
            status = 'approved_by_ai'
        else:
            status = 'rejected_by_ai'
        loan.status = status
        loan.save()

        print(f'[CELERY - SUCCESS] Updating status to {status} on Loan {loan} id {id}')
    except Loan.DoesNotExist:
        print(f'[CELERY - ERROR] Error while Updating status to {status} on Loan id {id}')
