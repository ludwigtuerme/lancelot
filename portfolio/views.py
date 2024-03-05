from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
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
      search_vector = \
          SearchVector("field_of_work", config="spanish", weight='D') \
        + SearchVector("work_experience", config="spanish", weight='A') \
        + SearchVector("projects", config="spanish", weight='B')
      search_query = SearchQuery(query, config="spanish")
      results = Portfolio.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
      ).filter(rank__gte=0.3).order_by('-rank')

  return render(request,
                "portfolio/search.html",
                {"form": form,
                 "query": query,
                 "results": results,
                })

def search_category(request, category):
  form = SearchForm()
  query = Portfolio.WorkAreas[category].label
  results = Portfolio.objects.filter(field_of_work=category)

  return render(
    request,
    "portfolio/search.html",
    {
      "form": form,
      "query": query,
      "results": results,
    }
  )
