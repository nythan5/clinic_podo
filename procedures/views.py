from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib import messages
from procedures.forms import ProcedureForm
from procedures.models import Procedure


class ProcedureCreateView(CreateView):
    model = Procedure
    form_class = ProcedureForm
    template_name = 'procedures/create.html'
    success_url = reverse_lazy('patients:patient_list')

    def form_valid(self, form):
        messages.success(
            self.request, f"Registrado o procedimento {form.instance.name} com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, f"Erro ao cadastrar o paciente {form.instance.name}.")
        return super().form_invalid(form)


class ProcedureDeleteView(DeleteView):
    model = Procedure
    success_url = reverse_lazy('patients:patient_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(
            self.request, f"Procedimento {self.object.name} deletado com sucesso!")
        return super().delete(request, *args, **kwargs)
