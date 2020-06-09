from django.shortcuts import render, redirect

# Create your views here.
from board.forms import BoardForm
from board.models import Board
from fcuser.models import Fcuser


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)

    return render(request, 'board_detail.html', {'board': board})


def board_list(request):
    boards = Board.objects.all().order_by('-id')

    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board = Board()

            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(username=user_id)

            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['contents']
            board.writer = fcuser

            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})
