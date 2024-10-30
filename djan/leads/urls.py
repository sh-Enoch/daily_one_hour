from .views import home_page, leads_list, lead_view
from  django.urls import path


app_name = 'leads'

urlpatterns = [
    path('', home_page),
    path('all/', leads_list),
    path('<pk>/', lead_view),
]
