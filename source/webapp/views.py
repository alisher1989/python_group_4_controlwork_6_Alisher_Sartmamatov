from django.shortcuts import render
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
