from django.urls import path
from observations import views

urlpatterns = [
    path('observations/', views.ObservationList.as_view()),
    path('observations/<int:pk>/', views.ObservationDetail.as_view()),
]