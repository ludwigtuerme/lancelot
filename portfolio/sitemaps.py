from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.text import slugify
from .models import Portfolio

from datetime import date

class StaticViewSitemap(Sitemap):
  changefreq = "daily"

  def items(self):
    labels = []
    for area in Portfolio.WorkAreas:
      labels.append(slugify(area.label))
    return labels

  def location(self, areas):
    return reverse("portfolio:category", args=[areas])
