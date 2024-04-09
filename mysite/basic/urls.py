from django.urls import path
from .views import IndexView, ObjectsListView, ObjectView

urlpatterns = [
	path("", IndexView.as_view()),
	path("fullList", ObjectsListView.as_view()),
	path("object<int:pk>", ObjectView.as_view())
	]