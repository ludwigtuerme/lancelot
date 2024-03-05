from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
  path("search/", views.portfolio_search, name="search"),
  path("search/<slug:category>/", views.search_category, name="category"),
]
