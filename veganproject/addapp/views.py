from django.shortcuts import render, redirect
from veganapp.models import VeganFood
from .forms import AddFood
# Create your views here.
def add_food(request):
    form=AddFood()
    print(request.method)
    if request.method=='POST':
        form=AddFood(request.POST,request.FILES)
        if form.is_valid():
            VeganFood.objects.create(**form.cleaned_data)
            print("new food created")
            return redirect('/vegan/')
        else:
            print(form.errors)
    return render(request,'add.html',dict(form=form))