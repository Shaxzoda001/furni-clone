from django.shortcuts import render
from django.views.generic import TemplateView
from main_app.models import Shop

# Create your views here.


class HomePageView(TemplateView):
    def get(self, request):
        context = {}
        temp = Shop.objects.all()
        context['data'] = temp
        return render(request, 'main/index.html', context)

