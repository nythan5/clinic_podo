from django.contrib import admin
from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'medical_record_number',
                    'date_of_birth', 'is_active', 'last_schedule_date')
    search_fields = ('first_name', 'last_name', 'medical_record_number')
    list_filter = ('is_active', 'date_of_birth', 'last_schedule_date')
    ordering = ('last_name', 'first_name')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'medical_record_number')
        }),
        ('Status', {
            'fields': ('is_active', 'last_schedule_date'),
            'description': 'Informações sobre a situação do paciente e último agendamento.'
        }),
        ('Contato', {
            'fields': ('phone_1', 'phone_2', 'email'),
            'description': 'Informações de contato do paciente.'}),
        ('Gênero', {'fields': ('gender',)}),
    )

    readonly_fields = ('medical_record_number',)
