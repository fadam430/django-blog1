from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
]
