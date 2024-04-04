from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Game, User

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="basic/index.html")


class GameListView(ListView):
    model = Game
    template_name = "basic/gameList.html"
    paginate_by = 50

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, status=200)