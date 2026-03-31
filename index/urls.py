from django.urls import path, include
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('dates/<str:monthAndDate>', views.dates, name='date'),
    path('datawizard/', include('data_wizard.urls')),
]