from django.conf import settings


def environment(request):
    """
    Adiciona a variável ENVIRONMENT a todos os templates.
    """
    return {
        "ENVIRONMENT": getattr(settings, "ENVIRONMENT", "Desenvolimento")
    }
