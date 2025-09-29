from django.db import models
from patients.models import Patient


class Procedure(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='procedures',
        help_text="Paciente relacionado ao procedimento"
    )
    name = models.CharField(
        max_length=100,
        help_text="Nome do procedimento realizado"
    )
    procedure_date = models.DateField(
        help_text="Data em que o procedimento foi realizado"
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Observações adicionais sobre o procedimento"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-procedure_date']
        verbose_name = "Procedimento"
        verbose_name_plural = "Procedimentos"

    def __str__(self):
        return f"{self.name} ({self.procedure_date.strftime('%d/%m/%Y')}) - {self.patient}"
