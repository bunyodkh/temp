from django.urls import path

app_name = 'consultants'

from .views import (
    index,
    get_consultants,
    get_consultant,
    add_consultant,
    contibute
) 

urlpatterns = [
    path('', index, name='index'),
    path('consultants/', get_consultants, name='consultants-all'),
    path('consultant/<int:pk>', get_consultant, name='consultant-detail'),
    path('consultant/add', add_consultant, name='consultant-add'),
    path('contribute/', contibute, name='contribute')
]
