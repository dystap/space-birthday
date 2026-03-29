from django.urls import path, include
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('info/<int:id>', views.Info, name='info'),
    path('fillform', views.fillform, name='fillform'),
    path('dates/<int:id>', views.dates, name='date'),
    path('fillform/submit', views.submitform, name='submitform'),
    path('datawizard/', include('data_wizard.urls')),
]