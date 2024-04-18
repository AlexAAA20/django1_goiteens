from django.urls import path
from .views import IndexView, ObjectsListView, ObjectView, AboutView, RegisterView, LoginView, LogoutView

urlpatterns = [
	path("", IndexView.as_view(), name="index"),
	path("object", ObjectsListView.as_view()),
	path("object/<int:pk>", ObjectView.as_view()),
	path("info", AboutView.as_view()),
	path("register", RegisterView.as_view()),
	path("login", LoginView.as_view()),
	path("logout", LogoutView.as_view())
	]