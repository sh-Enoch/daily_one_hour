from django.urls import path
from .views import snippet_list, snippet_detail


urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]