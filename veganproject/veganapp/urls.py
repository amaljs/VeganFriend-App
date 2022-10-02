from django.urls import path

from veganapp import views
app_name='veganapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:f_slug>/',views.FoodByOrgan,name='foodbyorgan'),
    path('<slug:o_slug>/<slug:f_slug>/',views.fooddetail,name='fooddetailsingle'),



]