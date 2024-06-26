from django.urls import re_path, path, include
from ctspi import views
from ctspi.forms import *

urlpatterns = [
     path("accounts/", include("django.contrib.auth.urls")),
     re_path(r'departments/.*', views.departments),
     re_path(r'blog/.*', views.blog, name='event-list'),
     path('search/', views.event_search, name='post_search'),
     path('player/', views.player, name='player'),
     # CRUD
     path('event/new/', views.EventCreateView.as_view(), name='event-create'),
     path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
     path('event/<int:pk>/update/',
          views.EventUpdateView.as_view(), name='event-update'),
     path('event/<int:pk>/delete/',
          views.EventDeleteView.as_view(), name='event-delete'),
    path('new_event/', EventWizard.as_view()),

     re_path(r'\w*', views.main),
     re_path(r'.*', views.ctspi_404),
]
