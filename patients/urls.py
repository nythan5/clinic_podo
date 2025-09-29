from django.urls import path
from patients.views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView

app_name = 'patients'

urlpatterns = [
    path('list/', PatientListView.as_view(), name='patient_list'),
    path('add/', PatientCreateView.as_view(), name='patient_add'),  # noqa
    path('edit/<int:pk>/', PatientUpdateView.as_view(), name='patient_edit'),  # noqa
    path('delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),  # noqa

]
