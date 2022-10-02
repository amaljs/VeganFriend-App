from django.db import models

# Create your models here.
from django.urls import reverse

Choices=(
    ('Eye','Eye'),
    ('Hair','Hair'),
    ('Brain','brain'),
    ('Lungs','lungs'),
    ('Heart','heart'),
    ('Muscles','Muscles'),
    ('Bones',"Bones"),
    ('Skin','Skin'),
    ('Bowels',"Bowels")
)

class Organ(models.Model):
    name=models.CharField(max_length=50,unique=True,choices=Choices)
    slug=models.SlugField(max_length=50,unique=True)
    image=models.ImageField(upload_to='organ_pics',blank=True)
    desc=models.TextField()

    def get_organ(self):
        return  reverse('veganapp:foodbyorgan',args=[self.slug])

    class Meta:
        ordering=['name',]
        verbose_name='organ'
        verbose_name_plural='organs'

    def __str__(self):
        return self.name

class VeganFood(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    image=models.ImageField(upload_to='food_pics',blank=True)
    desc=models.TextField()
    organ=models.ForeignKey(Organ,on_delete=models.CASCADE)

    def get_food(self):
        return reverse('veganapp:fooddetailsingle',args=[self.organ.slug,self.slug])

    class Meta:
        ordering=['name',]
        verbose_name='food'
        verbose_name_plural='foods'

    def __str__(self):
        return self.name




