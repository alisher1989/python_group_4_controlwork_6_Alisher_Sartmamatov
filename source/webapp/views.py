from django.shortcuts import render, redirect
from webapp.forms import GuestbookForm
from webapp.models import Guestbook


def index_view(request, *args, **kwargs):
    search_query = request.GET.get('search', '')
    if search_query:
        items = Guestbook.objects.filter(title__icontains=search_query)
    else:
        items = Guestbook.objects.all()
    return render(request, 'index.html', context={
        'items': items
    })


def item_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = GuestbookForm()
        return render(request, 'add.html', context={'form': form})
    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            item = Guestbook.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
            return redirect('index', pk=item.pk)
        else:
            return render(request, 'add.html', context={'form': form})