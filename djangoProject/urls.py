"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from leads.views import hello
from leads.models import Lead, MeanOfTransportation
from leads.views import delete_lead, LeadCreateView, LeadsView, compare_volumes, LeadListView, LandingPageView


admin.site.register(Lead)
admin.site.register(MeanOfTransportation)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LandingPageView.as_view(), name="landing.html"),
    #path("hello/<s0>", hello),
    path("delete/<customer_name>",delete_lead),
    path("leads/", LeadListView.as_view(), name="leads.html"),
    path("add_lead/", LeadCreateView.as_view(), name="lead_form.html"),
    path("compare_volumes", compare_volumes),
]
