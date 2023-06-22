from django import forms
from django.contrib import admin
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'cpf': 'CPF',
            'status': 'Status',
            'requested_infos': 'Requisitar informações adicionais'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['cpf'].disabled = True

        limited_choices = (
            ('approved_by_human', 'Aprovado'),
            ('rejected_by_human', 'Rejeitado'),
        )
        self.fields['status'].choices = limited_choices

class LoanAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'name', 'status')
    form = LoanForm

admin.site.register(Loan, LoanAdmin)