from django.shortcuts import render, HttpResponse
from .models import Lead

# Create your views here.
def home_page(request):
    return render(request, "mains.html")

def leads_list(request):
    lead = Lead.objects.all()
    context = {
        "leads": lead
    }
    return render(request, 'leads_list.html', context)

def lead_view(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    
    return render(request, 'lead_detail.html',context)


