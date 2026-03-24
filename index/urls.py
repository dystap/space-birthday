from django.urls import path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.home, name='home'),
    path('info/<int:id>', views.Info, name='info'),
    path('fillform', views.fillform, name='fillform'),
    path('fillform/submit', views.submitform, name='submitform'),

]