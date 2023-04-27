from django.urls import path
from likes import views
urlpatterns = [
    path('likes/', views.LikeList_as.view()),
]