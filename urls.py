from django.urls import re_path, path, include
from ctspi import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    re_path(r'departments/.*', views.departments),
    re_path(r'blog/.*', views.blog, name='event-list'),
    path('search/', views.event_search, name='post_search'),
    # CRUD
    path('event/new/', views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/update/',
         views.EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/',
         views.EventDeleteView.as_view(), name='event-delete'),

    re_path(r'\w*', views.main),
    re_path(r'.*', views.ctspi_404),
]
