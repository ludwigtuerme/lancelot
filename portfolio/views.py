from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render, HttpResponse
from .forms import SearchForm
from .models import Portfolio

def index(request):
    return render(request, "index.html")

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
  query = None

  # Linear-time lookup... But it's not a bottleneck yet.
  from django.utils.text import slugify
  for area in Portfolio.WorkAreas:
    if slugify(area.label) == category:
      category = area
      query = category.label

  if query is None:
    return HttpResponse(f"'{category}' no es una categoría válida.")

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
