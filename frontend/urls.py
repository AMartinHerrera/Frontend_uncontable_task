from django.urls import path

from . import views

urlpatterns = [
    
    #Optional, in order to let it run with just url: /world
    path('', views.home, name='home'),
    path('exp_details/', views.exp_details, name='exp_details'),
    path('scatterplot_tool/', views.scatterplot_tool, name='scatterplot_tool'),

]