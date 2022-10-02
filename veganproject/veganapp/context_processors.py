from .models import  Organ

def menu_links(request):
    links=Organ.objects.all()
    return dict(links=links)