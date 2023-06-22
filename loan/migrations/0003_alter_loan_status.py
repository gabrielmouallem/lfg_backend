# Generated by Django 4.2.2 on 2023-06-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_loan_requested_infos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('processing', 'Processando'), ('approved_by_ai', 'Aprovado pela IA'), ('approved_by_human', 'Aprovado'), ('rejected_by_ai', 'Reprovado'), ('rejected_by_human', 'Reprovado')], default='processing', max_length=20),
        ),
    ]
