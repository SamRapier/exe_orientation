from django.urls import path

from . import views

urlpatterns = [
               path('', views.index, name='index'),
               path('health', views.health, name='health'),
               path('404', views.handler404, name='404'),
               path('500', views.handler500, name='500'),
			   path('MVP_treasure_hunt', views.MVP_treasure_hunt, name='MVP_treasure_hunt'),
               ]
