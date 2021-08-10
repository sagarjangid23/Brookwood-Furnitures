from .models import Category

def menu_links(requets):
    links=Category.objects.all()
    return dict(links=links)
