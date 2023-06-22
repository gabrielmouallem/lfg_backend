from django.db import models
from django.core.validators import RegexValidator

class Loan(models.Model):
    CPF_REGEX = '^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    cpf_validator = RegexValidator(
        regex=CPF_REGEX,
        message='CPF must be in the format XXX.XXX.XXX-XX'
    )

    STATUS_CHOICES = (
        ('processing', 'Processando'),
        ('approved_by_ai', 'Aprovado pela IA'),
        ('approved_by_human', 'Aprovado'),
        ('rejected_by_ai', 'Reprovado'),
        ('rejected_by_human', 'Reprovado'),
    )

    cpf = models.CharField(max_length=14, validators=[cpf_validator], unique=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    requested_infos = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name} - {self.cpf} - {self.status}"