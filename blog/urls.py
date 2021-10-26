from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="index_url"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail_url"),
    path("post/create", views.PostCreate.as_view(), name="post_create_url"),
]