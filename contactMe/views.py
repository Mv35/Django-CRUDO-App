from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from . forms import ContactForm


class ContactView(View):
    form_class = ContactForm
    initial = {'key':'value'}
    template_name = 'contactMe/form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            form = self.form_class()

        return render(request, self.template_name, {'form': form})
