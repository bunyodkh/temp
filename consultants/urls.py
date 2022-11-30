from django.urls import path

app_name = 'consultants'

from .views import (
    index,
    get_consultants,
    get_consultant,
    contibute
) 

urlpatterns = [
    path('', index, name='index'),
    path('consultants/', get_consultants, name='consultants-all'),
    path('consultants/<int:pk>', get_consultant, name='consultant-detail'),
    path('contribute/', contibute, name='contribute')
]
