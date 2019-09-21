
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import GuestbookForm
from webapp.models import Guestbook, STATUS_CHOICES


def index_view(request, *args, **kwargs):

    search_query = request.GET.get('search', '')
    if search_query:
        items = Guestbook.objects.filter(author__icontains=search_query)

    else:
        items = Guestbook.objects.all().filter(status='active').order_by('-created_at')
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
            return redirect('index')
        else:
            return render(request, 'add.html', context={'form': form})


def item_edit_view(request, pk):
    item = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
        form = GuestbookForm(data={
            'author': item.author,
            'email': item.email,
            'text': item.text,

        })
        return render(request, 'edit.html', context={'form': form, 'item': item})
    elif request.method == 'POST':
        form = GuestbookForm(data=request.POST)
        if form.is_valid():
            item.author = form.cleaned_data['author']
            item.email = form.cleaned_data['email']
            item.text = form.cleaned_data['text']
            item.save()
            return redirect('index')
        else:
            return render(request, 'edit.html', context={'form': form, 'item': item})


def item_delete_view(request, pk):
    item = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'item': item})
    elif request.method == 'POST':
        item.delete()
        return redirect('index')