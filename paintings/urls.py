from django.urls import path
from paintings import views

urlpatterns = [
    path('paintings/', views.PaintingList.as_view()),
    path('paintings/<int:pk>/', views.PaintingDetail.as_view()),
]