from django.urls import path

from addapp import views

app_name='addapp'

urlpatterns=[
        path('',views.add_food,name='addfood'),
]