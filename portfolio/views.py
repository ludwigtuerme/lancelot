from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from .forms import SearchForm
from .models import Portfolio

def portfolio_search(request):
  form = SearchForm()
  query = None
  results = []

  if "query" in request.GET:
    form = SearchForm(request.GET)
    if form.is_valid():
      query = form.cleaned_data["query"]
      results =  Portfolio.objects.annotate(
        search=SearchVector("field_of_work", "work_experience", "projects"),
      ).filter(search=query)

  return render(request,
                "portfolio/search.html",
                {"form": form,
                 "query": query,
                 "results": results,
                })
