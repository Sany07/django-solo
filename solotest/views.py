
# For Class-based views we import.

from django.views.generic import TemplateView

class Home(TemplateView):
    
    template_name="index.html"
