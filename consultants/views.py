from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Consultant


def index(request):
    context = { 'title' : 'TEST PAGE' }
    return render(request, 'index.html', context)


def get_consultants(request):
    consultants = get_list_or_404(Consultant)
    context = { 'title': 'Consultants List', 'consultants': consultants }
    return render(request, 'consultants.html', context)


def get_consultant(request, *args, **kwargs):
    pk = kwargs.get('pk')
    consultant = get_object_or_404(Consultant, pk=pk)
    context = { 'title': 'Consultant Detail', 'consultant': consultant }
    return render(request, 'consultant.html', context)


def contibute(request):
    context = { 'title': 'Contribute data or knowledge'}
    return render(request, 'contribute.html', context)

