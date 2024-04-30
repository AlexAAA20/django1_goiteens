from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView, DetailView
from .models import Object, User, Tag
from django.db.models import Q
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, CreateFastForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="basic/index.html", context={"req": request})


class ObjectsListView(ListView):
    model = Object
    template_name = "basic/objectList.html"
    paginate_by = 50


class ObjectView(DetailView):
    model = Object
    template_name = "basic/objectShow.html"
    context_object_name = 'object'


class AboutView(View):
    template_name = "basic/about.html"

    def get(self, request, *args, **kwargs):
        return render(request, template_name="basic/about.html")


class RegisterView(View):
    form_class = RegisterForm
    initial = {"key": "value"}
    template_name = "basic/signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, template_name="basic/signup.html", context={"form": form, "request": request})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not request.user.is_authenticated:
            if form.is_valid():
                raw_password = form.cleaned_data["password"]
                repeat_password = form.cleaned_data["repeat_password"]

                username = form.cleaned_data["username"]
                if raw_password == repeat_password:
                    user = User.objects.create(username=username)
                    user.set_password(raw_password)
                    print(user.password)
                    print(user.username)
                    user.save()
                    login(request, user)
                    return redirect("index")
        else:
            return render(request, self.template_name, {"form": form, "request": request})
        return render(request, self.template_name, {"form": form, "request": request})


class LoginView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = "basic/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, template_name="basic/login.html", context={"form": form, "request": request})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not request.user.is_authenticated:
            if form.is_valid():
                password = form.cleaned_data["password"]

                username = form.cleaned_data["username"]

                users_wtsu = User.objects.filter(username=username)
                if len(users_wtsu) == 1:
                    user = authenticate(
                        username=username,
                        password=password
                        )
                    if user:
                        login(request, user)
                        return redirect("index")
        else:
            return render(request, self.template_name, {"form": form, "request": request})
        return render(request, self.template_name, {"form": form, "request": request})


class LogoutView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = "basic/logout.html"

    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("index")

class CreateAFastObject(View):
    form_class = CreateFastForm
    initial = {"key": "value"}
    template_name = "basic/quick_create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            url = form.cleaned_data["url"]
            tags = form.cleaned_data["tags"].split(",")
            all_tags = Tag.objects.filter(name__in=tags)

            # Create new tags if they don't exist
            for tag in tags:
                if not all_tags.filter(name=tag).exists():
                    new_tag = Tag.objects.create(name=tag)
                    all_tags |= Tag.objects.filter(pk=new_tag.pk)

            new_object = Object.objects.create(name=name, description=description, url=url, creator=request.user)
            new_object.tags.set(all_tags)
            return redirect("index")

        return render(request, self.template_name, context={"form": form})


class TerminateAccountView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = "basic/terminate.html"

class TestView(View):
    template_name = "basic/tools/example.html"

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, context={"req": request})
