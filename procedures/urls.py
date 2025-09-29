from django.urls import path
from procedures.views import ProcedureCreateView, ProcedureDeleteView

app_name = 'procedures'

urlpatterns = [
     path('add/', ProcedureCreateView.as_view(), name='procedure_add'),  # noqa
    # path('edit/<int:pk>/', PatientUpdateView.as_view(), name='patient_edit'),  # noqa
    path('delete/<int:pk>/', ProcedureDeleteView.as_view(), name='procedure_delete'),  # noqa

]
