from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
from  django.urls import path


app_name = 'leads'

urlpatterns = [
    path('all/', LeadListView.as_view(), name="lead_list"),
    path('<int:pk>/', LeadDetailView.as_view(),name="lead_view"),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead_delete"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
]
