from django.shortcuts import render
from veganapp.models import VeganFood
from django.db.models import Q

# Create your views here.
def search_result(request):
    query=None
    foods=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        foods=VeganFood.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))


    return  render(request,'search.html',dict(query=query,foods=foods))



