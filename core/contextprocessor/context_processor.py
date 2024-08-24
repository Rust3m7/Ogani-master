from core.models import Setting

def get_setting(request):
    context={
        'setting': Setting.objects.first()
    }
    return context