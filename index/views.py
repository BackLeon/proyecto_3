from django.shortcuts import render, redirect
from publication.models import Publication, ProfileUser, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from publication.models import Relationship


# Create your views here.

@login_required
def index(request):

    pub = Publication.objects.all()
    context = {
        "pub": pub
    }


    return render(request, "index/index.html", context)



class Profile(LoginRequiredMixin, ListView):
    model = Publication
    template_name = "index/profile.html"
    context_object_name = "prof"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prof"] = context["prof"].filter(user=self.request.user)
        context["count"] = context["prof"].filter().count
        return context



@login_required
def ViewProfile(request, id):

    prof = User.objects.get(id=id)
    pub = Publication.objects.filter(user_id=id)

    context = {
        "prof": prof,
        "pub": pub
    }

    return render(request, "index/viewprofile.html", context)


class ViewPublication(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = "index/viewpublication.html"
    context_object_name = "pubview"


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "index/updateprofile.html"
    context_object_name = "prof"
    success_url = reverse_lazy("index")
    fields = [
        "username",
        "first_name",
        "last_name",
        "email"
    ]


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect("index")

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship.objects.filter(from_user=current_user.id).get()
    rel.delete()
    return redirect("index")


