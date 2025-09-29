from django.db.models.signals import pre_save
from django.dispatch import receiver
from patients.models import Patient

PREFIX = "PT"  # abreviação do paciente


@receiver(pre_save, sender=Patient)
def set_medical_record_number(sender, instance, **kwargs):
    """
    Gera um número de prontuário sequencial do tipo:
    PT0001, PT0002, ...
    """
    if not instance.medical_record_number:
        # Pega o último número sequencial registrado
        last_patient = Patient.objects.filter(
            medical_record_number__startswith=PREFIX
        ).order_by('-medical_record_number').first()

        if last_patient:
            # Extrai apenas a parte numérica do último prontuário
            last_number = int(last_patient.medical_record_number[len(PREFIX):])
            next_number = last_number + 1
        else:
            next_number = 1

        # Preenche com zeros à esquerda para ter 4 dígitos
        instance.medical_record_number = f"{PREFIX}{next_number:04d}"
