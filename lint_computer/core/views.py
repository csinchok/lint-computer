from django.http import Http404

from django.shortcuts import render, get_object_or_404

from .models import Repository


def repository_detail(request, pk=None, name=None):

    if pk:
        repo = get_object_or_404(Repository, pk=pk)
    elif name:
        repo = get_object_or_404(Repository, name=name)
    else:
        raise Http404

    return render(request, 'repository_detail.html', context={'repo': repo})
