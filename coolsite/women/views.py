from django.shortcuts import render
from women.models import Women
# Create your views here.

# def index(request):
#     return render(request, "index.html")
def about(request):
    return render(request, "about.html")
menu = ["O сайте", "добавить статью", "обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    data = {'menu': menu, 'title': 'Главный страница', 'posts': posts}
    return render(request, "index.html", data)