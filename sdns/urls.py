from django.urls import path
from . import views

urlpatterns = [
   path('', views.RegisterListView.as_view(), name='register_list') ,
   path("add/", views.RegisterCreateView.as_view(), name='register_add'),
   path("delete/", views.RegisterBulkDeleteView.as_view(), name='register_bulk_delete'),
   path('<int:pk>/', views.RegisterView.as_view(), name='register'),
   path('<int:pk>/edit/', views.RegisterEditView.as_view(), name='register_edit'),
   path('<int:pk>/delete/', views.RegisterDeleteView.as_view(), name='register_delete'),
]