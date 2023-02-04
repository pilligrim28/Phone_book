from django.views.generic import TemplateView, CreateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models


class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["persones"] = models.Persone.objects.all()
        return context


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(
                phone=phone_number, contact=self.object)
        return super().get_success_url()

class DeletePhoneFormView(DeleteView):
    model = models.Persone
    template_name = 'phonebook/delete_persone.html'
    success_url = reverse_lazy('home')