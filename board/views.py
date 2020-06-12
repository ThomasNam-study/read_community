from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from board.forms import BoardForm
from board.models import Board
from boardtag.models import BoardTag
from fcuser.models import Fcuser


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)

        return render(request, 'board_detail.html', {'board': board})
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')

    page = request.GET.get('p', 1)
    paginator = Paginator(all_boards, 10)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login')

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():

            tags = form.cleaned_data['tags'].split(',')

            board = Board()

            user_id = request.session.get('user')
            user = Fcuser.objects.get(id=user_id)

            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['contents']
            board.writer = user

            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = BoardTag.objects.get_or_create(name=tag)

                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})
