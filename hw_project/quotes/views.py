from django.shortcuts import render

# Create your views here.

from .utils import get_mongodb

# def main(request, page):
#     db = get_mongodb()
#     quotes = db.quotes.find()
#     per_page = 10
#     paginator = paginator(list(quotes), per_page)
#     quotes_on_page = paginator.page(page)
#     return render(request, "quotes/index.html", context={'quotes': quotes_on_page})

def main(request):
    db = get_mongodb()
    quotes = db.quotes.find()

    return render(request, "quotes/index.html", context={'quotes': quotes})