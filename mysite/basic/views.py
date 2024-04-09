from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Object, User

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="basic/index.html")


class ObjectsListView(ListView):
    model = Object
    template_name = "basic/objectList.html"
    paginate_by = 50

class ObjectView(DetailView):
    model = Object
    template_name = "basic/objectShow.html"
    context_object_name = 'object'