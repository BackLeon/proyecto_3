from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publication

# Create your views here.

class NewPublication(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = "publication/newpublication.html"
    context_object_name = "campnew"
    success_url = reverse_lazy("index")
    fields = [
        "category",
        "publication_name",
        "publication_description",
        "publication_image",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewPublication, self).form_valid(form)


class EditPublication(LoginRequiredMixin, UpdateView):
    model = Publication
    template_name = "publication/updatepublication.html"
    context_object_name = "uppubli"
    success_url = reverse_lazy("index")
    fields = [
        "category",
        "publication_name",
        "publication_description",
        "publication_image",
    ]


def deletepublication(request, id):
    p = Publication.objects.get(id=id)
    p.delete()

    return redirect("index")