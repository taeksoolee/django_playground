from importlib.resources import read_binary
from unittest import loader
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader


from board.models import BbsBoard


def index(request):
  return HttpResponse('hello, World. You\'re at the board index.')

# template
def list(request):
  # return HttpResponse('detail page!, ' + str(board_id))
  board_all_list = BbsBoard.objects.all()
  context = {
    'board_all_list': board_all_list
  }

  # 1. normal
  # template = loader.get_template('index.html')
  # return HttpResponse(template.render(context, request))

  # 2. short cut
  return render(request, 'index.html', context)

# path variable
# get_object_or_404
def detail(request, board_id):
  # 1. normal
  # try:
  #   b = BbsBoard.objects.get(pk=board_id)
  # except BbsBoard.DoesNotExist:
  #   raise Http404('Bbs does not exist')

  # return render(request, 'detail.html', {'board' : b})

  # 2. short cut
  b = get_object_or_404(BbsBoard, pk=board_id)
  return render(request, 'detail.html', { 'board': b })

