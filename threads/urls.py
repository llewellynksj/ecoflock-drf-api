from django.urls import path
from threads import views

urlpatterns = [
    path('threads/', views.ThreadList.as_view()),
    path('threads/<int:pk>/', views.ThreadDetail.as_view()),
]
