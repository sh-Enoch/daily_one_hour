from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Lead, Agent
from .forms import LeadCreate, LeadModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganiserLoginRequiredMixin
#
class LandingPageView(TemplateView):
    template_name = "mains.html"

# Create your views here.
def landing_page(request):
    return render(request, "mains.html")

#create a signup view
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

#create a class based  list view
class LeadListView(LoginRequiredMixin, ListView):
    template_name ="leads_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation= user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset


#create a class based detail view
class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_view(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    
    return render(request, 'lead_detail.html',context)

# craete a class based update view
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update_lead.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads/all/')
        
    context = {
        "lead":lead,
        "form":form
    }

    return render(request, 'update_lead.html', context)

#define a class based create view
class LeadCreateView(OrganiserLoginRequiredMixin, CreateView):
    template_name = 'create_lead.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


class LeadDeleteView(OrganiserLoginRequiredMixin, DeleteView):
    template_name = 'delete_lead.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_list")



# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print("Receiving data")
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()

#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             return redirect('/leads/all/')


#     context = {
#         "form": form
#     }

#     return render(request, 'create_lead.html', context)




