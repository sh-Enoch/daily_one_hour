from django.contrib import admin

# Register your models here.
from leads.models import Lead, Agent, User, UserProfile


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(Lead)