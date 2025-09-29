from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date


class Patient(models.Model):
    """ Modelo para armazenar informações do paciente """

    first_name = models.CharField(
        max_length=30,
        help_text="Primeiro nome do paciente",
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=30,
        help_text="Sobrenome do paciente",
        null=False,
        blank=False
    )

    date_of_birth = models.DateField(
        help_text="Data de nascimento do paciente"
    )

    medical_record_number = models.CharField(
        max_length=20,
        unique=True,
        help_text="Número do prontuário médico"
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Indica se o paciente está ativo"
    )

    last_schedule_date = models.DateField(
        null=True,
        blank=True,
        help_text="Data do último agendamento do paciente"
    )

    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')],
        help_text="Gênero do paciente"
    )

    phone_1 = PhoneNumberField(null=True, blank=True)
    phone_2 = PhoneNumberField(null=True, blank=True)

    email = models.EmailField(
        null=True,
        blank=True,
        help_text="Endereço de e-mail do paciente"
    )

    @property
    def age(self):
        """Retorna a idade do paciente em anos."""
        if not self.date_of_birth:
            return None
        today = date.today()
        return (
            today.year - self.date_of_birth.year -
            ((today.month, today.day) <
             (self.date_of_birth.month, self.date_of_birth.day))
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name} (P: {self.medical_record_number})"
