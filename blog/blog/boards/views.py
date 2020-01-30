from django.shortcuts import render, get_object_or_404
from .models import Board
# Create your views here.

from django.http import HttpResponse


def home(request):
    boards = Board.objects.all()

    return render(request, 'home.html', context={'boards': boards})

def board_topics(request, pk):

    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', context={'board': board})
