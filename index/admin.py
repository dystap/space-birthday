from django.contrib import admin
from index.models import info
import data_wizard
from index.models import date

admin.site.register(info)
data_wizard.register(date)
admin.site.register(date)