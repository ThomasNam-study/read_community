from django.http import HttpResponse
from django.shortcuts import render

from fcuser.models import Fcuser


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(id=user_id)

    return render(request, 'home.html')