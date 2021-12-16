from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from . import models

# Create your views here.
def say_smth(request):
    return HttpResponse(
        "Один из управляющих концлагеря делает у себя ремонт в коттедже. Приходит, спрашивает:— Не знаете кто может плитку положить?— Там вон молдаван повели в газовую камеру, иди у них спроси, может успеешь. Прибегает, дверь газовой камеры уже закрывается, но управляющий успевает подставить ногу и спрашивает:— Мужики, можете плитку в доме положить?— Ну можем 200 рублей за квадратУправляющий задумался— За 150 положите?— Ногу убрал")




def get_posts(request):
    post = models.Posts.objects.all()
    return render(request, 'post_list.html', {'post': post})


def post_detail(request, id):
    try:
        post = models.Posts.objects.get(id=id)
    except models.Posts.DoesNotExist:
        raise Http404("Post does not Exist")

    return render(request, "post_detail.html", {"post": post})