from django.urls import path
from posts.views import PostView, PostSpecificView

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>/', PostSpecificView.as_view()),
]
