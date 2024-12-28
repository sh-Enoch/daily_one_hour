from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from leads.models import Agent
from .forms import AgentModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()
    

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('agents:agent-list')


class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    queryset = Agent.objects.all()
    

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent-list')
    

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    queryset = Agent.objects.all()
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agent-list')
