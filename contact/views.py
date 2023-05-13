from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from .models import Contact
from pathlib import Path
from os import path
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404




def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

def all_contacts(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 9)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, "contact/allcontacts.html", {"contacts": contacts})