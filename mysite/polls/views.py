from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

def index(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', {'quotes': quotes})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.added_by = request.user
            quote.save()
            return redirect('index')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})