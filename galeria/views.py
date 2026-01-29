from django.shortcuts import render,get_object_or_404
from galeria.models import Player
# Create your views here.


def index(request):

    players = Player.objects.all()

    return render(request,'galeria/index.html',{"dados":players})

def player(request,player_id):
    player = get_object_or_404(Player,pk=player_id)

    return render(request,'galeria/player.html',{"player":player})