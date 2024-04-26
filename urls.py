from django.urls import re_path, path
from ctspi import views

urlpatterns = [
    path('anons', views.anons),
    path('write_anons', views.write_anons),
    re_path(r'departments/.*', views.departments),
    re_path(r'blog/.*', views.blog, name='event-list'),

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
