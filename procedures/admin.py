from django.contrib import admin
from procedures.models import Procedure


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'procedure_date', 'patient')
    search_fields = ('name', 'patient__first_name', 'patient__last_name')
    ordering = ('-procedure_date',)
