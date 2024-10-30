from django.contrib import admin

# Register your models here.
from leads.models import Lead, Agent, User


admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)