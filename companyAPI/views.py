from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.

class CompanyListView(View):
    def get(self, request):
        if('name' in request.GET):
            cList = Company.objects.filter(name__contains=request.GET['name'])
        else:
            cList = Company.objects.all()    
        return JsonResponse(list(cList.values()), safe=False)

class CompanyDetailView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))