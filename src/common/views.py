from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class SalesView(View):
    template_name = 'sales.html'

    def get(self, request):
        return render(request, self.template_name)

class OperationsView(View):
    template_name = 'operations.html'

    def get(self, request):
        return render(request, self.template_name)
