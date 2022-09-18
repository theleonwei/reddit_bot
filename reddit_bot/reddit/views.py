from django.views.generic import ListView

from .models import Lead

# Create your views here.
class LeadView(ListView):
    model = Lead
    template_name = 'lead_list.html'

lead_view = LeadView.as_view()
