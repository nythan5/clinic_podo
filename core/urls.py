
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


class TestPageView(TemplateView):
    template_name = "base.html"


urlpatterns = [
    path('test', TestPageView.as_view(), name='test'),
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls', namespace='patients')),
    path('procedures/', include('procedures.urls', namespace='procedures')),
]
