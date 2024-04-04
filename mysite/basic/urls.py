from django.urls import path
from .views import IndexView, GameListView

urlpatterns = [
	path("", IndexView.as_view()),
	path("fullList", GameListView.as_view())
	]