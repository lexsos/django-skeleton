from django.views.generic import ListView

from .models import TestModel


class TestView(ListView):

    template_name = 'testapp/test.html'
    model = TestModel
