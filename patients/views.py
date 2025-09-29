from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from patients.models import Patient
from django.db.models import Q
from patients.forms import PatientForm
from django.urls import reverse_lazy
from django.contrib import messages


class PatientListView(ListView):
    model = Patient
    template_name = 'patients/list.html'
    context_object_name = 'patients'
    paginate_by = 10
    ordering = ['first_name', 'last_name',]

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        status = self.request.GET.get('status', '')

        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(medical_record_number__icontains=search)
            )

        if status == 'ativo':
            queryset = queryset.filter(is_active=True)
        elif status == 'inativo':
            queryset = queryset.filter(is_active=False)

        return queryset


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/create.html'
    success_url = reverse_lazy('patients:patient_list')

    def form_valid(self, form):
        messages.success(
            self.request, f"Paciente {form.instance.first_name} criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, f"Erro ao cadastrar o paciente {form.instance.first_name}.")
        return super().form_invalid(form)


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/update.html'
    success_url = reverse_lazy('patients:patient_list')

    def form_valid(self, form):
        messages.success(
            self.request, f"Paciente {form.instance.first_name} atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, f"Erro ao atualizar o paciente {form.instance.first_name}.")
        return super().form_invalid(form)


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/list.html'
    success_url = reverse_lazy('patients:patient_list')

    def post(self, request, *args, **kwargs):
        patient = self.get_object()
        messages.success(
            self.request, f"Paciente {patient.first_name} excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
