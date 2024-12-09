from .views import leads_list, lead_view, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView
from  django.urls import path


app_name = 'leads'

urlpatterns = [
    path('all/', LeadListView.as_view(), name="lead_list"),
    path('<int:pk>/', LeadDetailView.as_view(),name="lead_view"),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', lead_delete, name="lead_delete"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
]
