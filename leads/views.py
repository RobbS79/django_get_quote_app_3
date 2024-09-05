from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import LeadForm
from .models import Lead
from .viz import viz_compare_volumes
import pandas as pd


def compare_volumes(request):
    leads = Lead.objects.all()
    leads_list = list(leads.values())
    leads_df = pd.DataFrame(leads_list)
    plot_html = viz_compare_volumes(leads_df)

    # Wrap the HTML in an HttpResponse
    return HttpResponse(plot_html)


def delete_lead(request,customer_name):
    try:
        lead = Lead.objects.get(customer_name=customer_name)
        lead.delete()
        # Now you can work with the 'lead' object
        print(lead)
        return HttpResponse("Deleted lead successfully")
    except Lead.DoesNotExist:
        print("No lead found with the given customer name.")


class LandingPageView(TemplateView):
    template_name = "landing_page.html"


class LeadListView(TemplateView):
    template_name = 'leads.html'  # Path to your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads'] = Lead.objects.all()  # Fetch all leads and add to context
        return context


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'lead_form.html'  # Update this with the actual template path
    success_url = reverse_lazy('leads.html')  # Update this with the actual URL name or path

    # Optionally, you can override methods like form_valid to customize behavior
    def form_valid(self, form):
        # You can add custom logic here if needed
        return super().form_valid(form)

class LeadsView(TemplateView):
    template_name = 'leads.html'
    #success_url = reverse_lazy('leads.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads'] = Lead.objects.all()
        return context




