from django.shortcuts import render, get_object_or_404
from .models import Organ,VeganFood


# Create your views here.
def index(request):
    organs=Organ.objects.all()

    return  render(request,'index.html',{'organs':organs})

def FoodByOrgan(request,f_slug):
    organ=get_object_or_404(Organ,slug=f_slug)
    foods=VeganFood.objects.all().filter(organ=organ)
    return render(request,'organ.html',dict(organ=organ,foods=foods))

def fooddetail(request,o_slug,f_slug):
    try:
        food = VeganFood.objects.get(organ__slug=o_slug, slug=f_slug)

    except Exception as e:
        raise e

    return render(request,'food.html',{'food':food})


