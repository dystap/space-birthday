from django.contrib import admin
import data_wizard
from index.models import date

data_wizard.register(date)
admin.site.register(date)