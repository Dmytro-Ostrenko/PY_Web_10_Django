from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Quote
from .forms import QuoteForm
from django.http import HttpResponse
from scrapy.crawler import CrawlerProcess
from .connectDB import get_mongodb



from .update_quotes import ScraperQuotesSpider
from .models import Author, Quote, Tag



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            return redirect('quote_detail', pk=quote.pk)
    else:
        form = QuoteForm()
    return render(request, 'quotes/quote_form.html', {'form': form})

def quote_detail(request, pk):
    quote = Quote.objects.get(pk=pk)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def run_scraping(request):
    process = CrawlerProcess()
    process.crawl(ScraperQuotesSpider)
    process.start()
    return HttpResponse("Scraping process initiated successfully.")


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render

# @login_required
# def quote_list_view(request):
#     quotes = Quote.objects.all()
#     return render(request, 'quotes/quote_list.html', {'quotes': quotes})