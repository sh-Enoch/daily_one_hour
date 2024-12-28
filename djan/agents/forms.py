from leads.models import Agent
from django.forms import ModelForm


class AgentModelForm(ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
    