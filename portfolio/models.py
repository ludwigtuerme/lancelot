from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.utils.translation import gettext_lazy as _

class Portfolio(models.Model):
  class WorkAreas(models.TextChoices):
    AGRO = "AGRO", _("Agriculture, Food, and Natural Resources")
    ARCH = "ARCH", _("Architecture and Construction")
    ARTS = "ARTS", _("Arts, Audio/Video Technology, and Communication")
    EDU = "EDU", _("Education and Training")
    GOV = "GOV", _("Government and Public Administration")
    HES = "HES", _("Health Science")
    IT = "IT", _("Information Technology")
    LPL = "LPL", _("Law, Public Safety, Corrections, and Security")
    MKT = "MKT", _("Marketing")
    STEM = "STEM", _("Science, Technology, Engineering, and Math")
    OTHER = "OTHER", _("Other")

  field_of_work = models.CharField(
    max_length=5,
    choices=WorkAreas,
    default=WorkAreas.OTHER,
  )

  work_experience = models.TextField(
    max_length=1000,
  )

  projects = models.TextField(
    max_length=1000,
  )
